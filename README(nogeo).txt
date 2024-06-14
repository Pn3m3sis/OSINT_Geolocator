Name: nogeo_filter.py

Description: This script filters out IPv4 addresses that can not be geolocated because of either being in a private range, or within ranges used for other purpouses. It takes a csv file with one column containing IPv4 addresses and returns a filtered list.

Prerequisites: 
Python
ipaddress
sys

Output: filtered_"filename.csv"

use:
python nogeo_filter.py "filename.csv"