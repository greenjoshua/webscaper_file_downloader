import csv
import requests

def download_csv(link_name, file_name):
    with requests.Session() as s:
        download = s.get(link_name)
        decoded_content = download.content.decode('utf-8')
    file = open(file_name + ".csv", 'wt')
    file.write(decoded_content)
