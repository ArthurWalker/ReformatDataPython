import sys
import csv
import re

def main():
    with open('../../Docs/GeoDirectoryData.csv','r') as fin, open('ReformatGeoDirectory.csv','w') as fout:
        csv_reader = csv.reader(fin, delimiter=',')
        csv_writer = csv.writer(fout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for line in csv_reader:
            if line[0]=='BUILDING_ID':
                pass
            new_line_list = line+[re.sub('NULL', '',' '.join(line[3:16]))]
            csv_writer.writerow(new_line_list)

if __name__ == '__main__':
    main()