import glob
import csv
import re
import json

# collects names of all csv file names in the folder except for mlp6.csv
def collect_all_csv_filenames():
    global read_files
    read_files = glob.glob("*.csv")
    read_files.remove('mlp6.csv')

# reads in all the csv and writes out to a single csv
def read_write_csv():
    # opens up a new csv file to store everyone's information
    with open('everyone.csv','w') as everyone:
        for files in read_files:
            for line in open(files,'r',encoding='utf-8-sig'):
                # removes BOM from beginning of some .csv files
                line.lstrip('\ufeff')
                # removes extra new lines at end of file
                line = line.rstrip('\n')
                # only add lines that have the right information (not empty, right info)
                if line and not line.startswith('#'):
                    # standardizes delimiter to ','
                    line = line.replace(", ",",")
                    everyone.write(line)
                    everyone.write('\n')
                else:
                    continue
        # removes final new line
        everyone.truncate(everyone.tell()-1)
        everyone.close()

# checks for whitespaces in the team name
def check_no_spaces():
    i = 0;
    with open("everyone.csv",'r') as everyone:
        csvreader = csv.reader(everyone, delimiter = ",")
        for row in csvreader:
            if row[4].isalnum():
                i = i + 1;
    everyone.close()


# uses regex to check if the team name is camel case
# camel case is defined here as consisting only of alphanumeric characters,
# starting with a capitalized letter, followed by lower case letters,
# and at least one repeating instance of a capital letter followed by lower case letters
def check_camel_case():
    camelCase = re.compile('[A-Z][a-z0-9]*[A-Z0-9][a-z0-9]+[A-Za-z0-9]*')
    i = 0;
    with open("everyone.csv",'r') as everyone:
        csvreader = csv.reader(everyone, delimiter = ",")
        for row in csvreader:
            if camelCase.match(row[4]):
                i = i + 1;
    print("Total number of team names that are camel case: " + str(i))
    everyone.close()

# writes out a json file for all csv data
def write_json():
    everyone = open('everyone.csv','r')
    csvreader = csv.DictReader(everyone)
    # defines field names
    csvreader.fieldnames = ("FirstName","LastName","NetID","GithubName","TeamName")
    for row in csvreader:
        jsonfile = open(row['NetID'] + '.json', 'w')
        out = json.dumps(row)
        jsonfile.write(out)
        jsonfile.close()
    everyone.close()

def main():
    collect_all_csv_filenames()
    read_write_csv()
    check_no_spaces()
    check_camel_case()
    write_json()

if __name__ == "__main__":
    main()
