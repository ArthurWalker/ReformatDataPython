import sys
import csv
import re
import replace_shortcut_county 
import replace_special_county_case
import replace_special_short_case

def execute_address(address):
    #Remove Special Characters
    new_address = re.sub(r"[\s\s\/\\\(\)\|\?\[\].,!@#~=_+^%\$&`\*\":-;<>]+",' ',address)
    #Replace special case
    new_address = replace_special_county_case.replace(new_address)
    #Replace Shortcut County
    new_address = replace_shortcut_county.replace(new_address)
    #Replace special shortcut
    new_address = replace_special_short_case.replace(new_address)
    return new_address

def execute_each_line(mprn,new_address):
    return [mprn,new_address,execute_address(new_address)]

def main():
    with open('../../../Docs/OpenData.csv','r') as fin,open ('ReformatOpenData.csv','w') as fout:
        csv_reader = csv.reader(fin, delimiter=',')
        count = 0
        csv_writer = csv.writer(fout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for line in csv_reader:
            if (count==50):
                break
            count+=1
            new_line=execute_each_line(line[0],line[2])
            csv_writer.writerow(new_line)

if __name__ == '__main__':
    main()