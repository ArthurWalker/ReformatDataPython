import csv
import sys
import re

def main():


    with open ('../../Docs/GeoDirectoryData.csv','r') as fin, open('Small_Geo_Data.csv','w') as fout:
        csv_reader = csv.reader(fin, delimiter=',')
        csv_writer = csv.writer(
            fout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        count =0
        for line in csv_reader:
            if (count ==1000):
                break
           
            csv_writer.writerow(line)
            count +=1

if __name__ == '__main__':
    main()