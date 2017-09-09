#from sys import argv #Warum funktioniert die Zeile mit dem Import nicht?
import sys
import csv

def main():
    with open(sys.argv[1], 'r') as csvfile:
        my_file = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in my_file:
            #print (row[4])
            emails = set()
            print (emails)
            if row[4] not in emails:
                   #writer.writerow(row)
                   emails.add(row[4])
                   #print (row[4])
                   #print (', '.join(row))
                   
                   
if __name__ == "__main__":
    main()
