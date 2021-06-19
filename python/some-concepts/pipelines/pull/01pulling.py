import csv
import itertools

# reading csv file, defining csv dialect & skiping header
def parse_data(fname):
	with open(fname) as f:
		dialect = csv.Sniffer().sniff(f.read(2000)) # reading 2k char to find file pattern 
		f.seek(0) # stepback
		next(f) # skiping header
		yield from csv.reader(f, dialect=dialect)

# reading 15 lines of parsed data from cars.csv
for row in itertools.islice(parse_data('cars.csv'), 15):
    print(row) 