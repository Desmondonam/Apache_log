# 1. Open the log file and read the content of the file and find all the IP addresses
# 2. Count the requests from the IPs
# 3. write data to a CSV file. this isthe one that will be used in the next project

import re
import csv
from collections import Counter

def reader(filename):
    with open(filename) as f:
        log = f.read()

        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}'

        ips_list = re.findall(regexp, log)

        return ips_list


def count(ips_list):
    return Counter(ips_list)

def write_csv(counter):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        header= ['IP', 'Frequency']

        writer.writerow(header)

        for item in counter:
            writer.writerow( (item, counter[item]))




if __name__ == '__main__':
    write_csv(count(reader('D:/Akoko/Apache/Apache_log/week12_sample.log')))
