#!/usr/bin/python3

import csv
    
def main():
    newlist = []
    with open('superbirthday.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}') # python3.6 way
                                                              ## to do things
                print('Column names are {}'.format(", ".join(row)))
                line_count += 1
            # print(f'\t{row["name"]} aka {row["heroname"]} was born in {row["birthday month"]}.')
            # above is the python3.6+ way to do things
            print('\t{} aka {} was born in {}.'.format(row["name"],row["heroname"],row["birthday month"]))
            line_count += 1
            newlist.append([row["name"],row["birthday month"]])
    # print(f'Processed {line_count} lines.') # python3.6 way to do things
    print('Processed {} lines.'.format(line_count))
    
    with open('regularbirthday.csv', mode='w') as new_file:
        fieldnames = ['name', 'birthday month']
        writer = csv.writer(new_file, delimiter=',')
        for row in newlist:
          writer.writerow(row)

if __name__ == "__main__":
    main()
