import sys
import re
import csv


def processing_file(filename):
    count = 0
    with open(filename, 'r') as fin, open('Reformat2.csv', 'w') as fout:
        csv_reader = csv.reader(fin, delimiter=',')
        csv_writer = csv.writer(
            fout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        
        for line in csv_reader:
            if (line[1] != 'GEOGID'):
                line[1] = re.sub('SA2017_', '', line[1])
            count += 1
            if (count ==1000):
                break
            
            csv_writer.writerow(line)
#[0:int(len(line)/3)]

def main():
    processing_file('../../Docs/SAPS2016_SA2017.csv')


if __name__ == '__main__':
    main()