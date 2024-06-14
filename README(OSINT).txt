Name: OSINT_locator.py

Description: The script uses open source intelligence to geolocate IPv4 addresses through the application programming interface of www.ip-api.com. It will take a CSV file containing one column of an unspecified amount of IP addresses and use The API to find the following information: Country, Region, City, latitude, longitude, Internet service provider and Organization.

Prerequesits: 
Python
tqdm
requests
time
os

Output:	CSV file containing all IPv4 addresses with additional geolocation information.

Use: 
python OSINT_locator.py "path/filename.csv" 
optional: --output_file "filename.csv"
If output filename is not choosen it will default to location.csv.

