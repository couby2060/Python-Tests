#from sys import argv #Warum funktioniert die Zeile mit dem Import nicht?
import sys

def main():
    my_file = open(sys.argv[1], 'r')
    print (my_file.read())

if __name__ == "__main__":
    main()
