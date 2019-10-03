import csv
import requests

def download_csv(file_name):
    with requests.Session() as s:
        download = s.get(file_name)
        decoded_content = download.content.decode('utf-8')
    file = open('balls.csv', 'wt')
    file.write(decoded_content)
