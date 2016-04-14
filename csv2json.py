#!/usr/bin/python

import sys, getopt
import csv
import json

#csv2json script
def main(argv):
    csvfile = ''
    jsonfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:")
    except getopt.GetoptError:
        print 'csv2json.py -i <path to inputfile> -o <path to outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print 'csv2json.py -i <path to inputfile> -o <path to outputfile>'
            sys.exit()
        elif opt in ("-i", "--input"):
            csvfile = arg
        elif opt in ("-o", "--output"):
            jsonfile = arg

    def to_json(data):
        with open(jsonfile, "w") as file:
            file.write(json.dumps(data))
            file.write('\n')

    csv_rows = []
    with open(csvfile, "r") as file:
        reader = csv.DictReader(file)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        to_json(csv_rows)

if __name__ == "__main__":
    main(sys.argv[1:])
