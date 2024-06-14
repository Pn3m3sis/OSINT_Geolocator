import requests as rq
import time
import os
import csv
import argparse
from tqdm import tqdm

def main(file_path, output_file):
    global cache
    cache = []
    iplist = load_iplist(file_path)
    process_iplist(iplist)
    mkcsv(cache, output_file)

def genquery(*args):
    global cache
    json_payload = [{"query": arg, "fields": "query,country,regionName,city,lat,lon,isp,org"} for arg in args]
    retries = 5
    for attempt in range(retries):
        try:
            inquire = rq.post("http://ip-api.com/batch", json=json_payload).json()
            for info in inquire:
                for x, y in info.items():
                    cache.append(y)
            break  # Exit the retry loop if successful
        except Exception as e:
            #print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(5)  # Wait before retrying
            else:
                print("Failed to process the batch after multiple attempts.")


def process_iplist(iplist):
    batch_size = 100  # Number of IP addresses to process in each batch
    requests_per_minute_limit = 15  # Requests per minute
    seconds_per_minute = 60

    total_ips = len(iplist)
    processed_ips = 0
    start_time = time.time()

    with tqdm(total=total_ips) as pbar:
        while processed_ips < total_ips:
            batches_processed = 0
            while batches_processed < requests_per_minute_limit and processed_ips < total_ips:
                batch = iplist[processed_ips:processed_ips + batch_size]
                genquery(*batch)
                processed_ips += len(batch)
                pbar.update(len(batch))
                batches_processed += 1

            # Check if we need to wait to avoid exceeding the rate limit
            elapsed_time = time.time() - start_time
            if batches_processed >= requests_per_minute_limit and elapsed_time < seconds_per_minute:
                time_to_sleep = seconds_per_minute - elapsed_time
                time.sleep(time_to_sleep)
                start_time = time.time()

def load_iplist(file_path):
    iplist = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            iplist.extend(row)
    return iplist

def mkcsv(cache, output_file):
    with open(output_file, 'w', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        for i in range(0, len(cache), 8):
            row = cache[i:i+8]
            writer.writerow(row)
        print(f'The file {output_file} was created.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a CSV file containing IP addresses.")
    parser.add_argument('file_path', type=str, help='Path to the CSV file containing IP addresses.')
    parser.add_argument('--output_file', type=str, help='Name of the output CSV file.')
    args = parser.parse_args()

    output_file = args.output_file if args.output_file else "location.csv"
    main(args.file_path, output_file)