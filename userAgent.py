# 1. Open the log file and read the content of the file and find all the IP addresses
# 2. Count the requests from the User agents
# 3. write data to a CSV file. this isthe one that will be used in the next project

import re
import csv
from collections import Counter

def reader(filename):
    with open(filename) as f:
        log = f.read()
        #print(log)

        regexp = r"%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\""

        user_agent = re.findall(regexp, log)

        return user_agent


def count(agent_list):
    return Counter(agent_list)

def write_csv(counter):
    with open('useragent.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        header= ['User Agent', 'Frequency']

        writer.writerow(header)

        for item in counter:
            writer.writerow( (item, counter[item]))




if __name__ == '__main__':
    write_csv(count(reader('D:/Akoko/Apache/Apache_log/week12_sample.log')))
