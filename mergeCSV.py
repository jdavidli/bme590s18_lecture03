import glob
import csv

# collects names of all csv file names in the folder except for mlp6.csv
def collect_all_csv_filenames():
    global read_files
    read_files = glob.glob("*.csv")
    read_files.remove('mlp6.csv')
    #print(read_files)

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
                #print(line)
        everyone.truncate(everyone.tell()-1)
        everyone.close()

def check_no_spaces():
    i = 0;
    with open("everyone.csv",'r') as everyone:
        csvreader = csv.reader(everyone, delimiter = ",")
        for row in csvreader:
            print(row[4])
            if row[4].isalnum():
                i = i + 1;

    print(i)


def main():
    collect_all_csv_filenames()
    read_write_csv()
    check_no_spaces()

if __name__ == "__main__":
    main()
