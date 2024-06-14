import os
import glob
from scapy.all import rdpcap, conf, logging
import csv

def extract_unique_src_ips_from_pcap(folder_path):
    ip_addresses = set()
    
    # Suppress specific warnings from Scapy
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    
    # Use glob to find all pcap files in the folder
    pcap_files = glob.glob(os.path.join(folder_path, '*.pcap'))

    # Loop through each file found
    for file_path in pcap_files:
        try:
            packets = rdpcap(file_path)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
        
        # Extract unique source IP addresses from each packet
        for packet in packets:
            try:
                if packet.haslayer('IP'):
                    src_ip = packet['IP'].src
                    ip_addresses.add(src_ip)
            except Exception as e:
                print(f"Error processing packet in {file_path}: {e}")
    
    return list(ip_addresses)

def write_ip_addresses_to_csv(ip_addresses, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for ip in ip_addresses:
            writer.writerow([ip])

if __name__ == "__main__":
    folder_path = input("Enter the full folder path of pcap files: ")
    output_file = input("Enter the name of the file, include .csv in the end: ")

    ip_addresses = extract_unique_src_ips_from_pcap(folder_path)
    write_ip_addresses_to_csv(ip_addresses, output_file)
    print("CSV file containing unique source IP addresses has been created.")
