import sys
import re
import csv


def processing_file(filename):
    count = 0
    with open(filename, 'r') as fin, open('small_example.csv', 'w') as fout:
        csv_reader = csv.reader(fin, delimiter=',')
        csv_writer = csv.writer(fout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for line in csv_reader:
            if (count == 100):
                break
            if (line[15] == 'LONGFORD'):
                count += 1
                csv_writer.writerow(line)


def main():
    processing_file('../../Docs/GeoDirectoryData.csv')


if __name__ == '__main__':
    main()
