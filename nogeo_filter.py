import csv
import sys
import ipaddress

def is_in_range(ip):
    # Define the ranges
    ranges = [
        (ipaddress.IPv4Address('10.0.0.0'), ipaddress.IPv4Address('10.255.255.255')),  # Class A
        (ipaddress.IPv4Address('172.16.0.0'), ipaddress.IPv4Address('172.31.255.255')),  # Class B
        (ipaddress.IPv4Address('192.168.0.0'), ipaddress.IPv4Address('192.168.255.255')),  # Class C
        (ipaddress.IPv4Address('224.0.0.0'), ipaddress.IPv4Address('239.255.255.255')),  # Class D
        (ipaddress.IPv4Address('240.0.0.0'), ipaddress.IPv4Address('255.255.255.255')),  # Class E
        (ipaddress.IPv4Address('169.254.0.0'), ipaddress.IPv4Address('169.254.255.255'))  # DHCP
    ]

    # Check if the IP address is in any of the defined ranges
    for start, end in ranges:
        if start <= ip <= end:
            return True
    return False

def filter_ips(input_filename, output_filename):
    with open(input_filename, mode='r') as infile, open(output_filename, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            ip = ipaddress.IPv4Address(row[0])
            if not is_in_range(ip):
                writer.writerow([ip])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = 'filtered_' + input_filename

    filter_ips(input_filename, output_filename)
    print(f"Filtered IP addresses saved to {output_filename}")
