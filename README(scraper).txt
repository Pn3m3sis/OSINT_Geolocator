Name: PCAP_Scraper.py

Description: 
Python script that extracts Source IP addresses from PCAP files.

Prerequesits:
Python 3.7+
scapy (python library, can be downloaded with pip install scapy)

Output:	CSV file containing all unique source IP addresses from all files in specified folder.

Use: 
Program is made to be used in command line with python.
Initiate with: python scraper.py
Prompt will ask for path to folder containing the files to be read.
Prompt to choose name of the output file ending in ".csv".

Script will read all .pcap files in directory.
Errors will notify if files could not be read and specify which.
File will appear in the scripts directory.