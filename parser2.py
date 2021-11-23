import apache_log_parser

parser = apache_log_parser.make_parser('%h %l %u %t "%r" %s %B')
count = 0

with open('D:/Akoko/Apache/Apache_log/week12_sample.log') as in_f:
    for line in in_f:
        line = parser(line)
        count = count + 1
    print(count)