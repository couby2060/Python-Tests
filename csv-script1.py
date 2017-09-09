import sys
import csv
import re

def main():
    pattern = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    with open(sys.argv[1], 'r') as csvfile:
        my_file = csv.reader(csvfile, delimiter=';', quotechar='"')
        emails = set()
        for row in my_file:
            if row[4] not in emails:
                emails.add(row[4])
                if pattern.match(row[4]):
                    emails.add(row[4])
                    print(', '.join(row))
                   
if __name__ == "__main__":
    main()





