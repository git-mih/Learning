import csv
import itertools

# reading csv file, defining csv dialect & skiping header
def parse_data(fname):
	with open(fname) as f:
		dialect = csv.Sniffer().sniff(f.read(2000)) # reading 2k lines to find pattern and define dialect
		f.seek(0) # stepback
		next(f) # skiping header
		yield from csv.reader(f, dialect=dialect)

# filtering
def filter_data(data, word): # data is the parsed_data of cars.csv
	for row in data: 
		if word in row[0]:
			yield row

data = parse_data('cars.csv')
filtered_data = filter_data(data, 'Chevrolet')

print('\nFILTER USING: (Chevrolet)')
for row in itertools.islice(filtered_data, 10):
	print(row)


#______________________________________________________________
print('\nCHAINING FILTERS: (Chevrolet, Carlo)')
# chaining filters
data = parse_data('cars.csv')
filter_1 = filter_data(data, 'Chevrolet')
filter_2 = filter_data(filter_1, 'Carlo')

for row in filter_2:
	print(row)


#______________________________________________________________
# lets hard coding it
def pipeline():
	data = parse_data('cars.csv')
	filter_1 = filter_data(data, 'Chevrolet')
	filter_2 = filter_data(filter_1, 'Carlo')
	yield from filter_2

results = pipeline()

print('\nHARDCODED PIPELINE: (Chevrolet, Carlo)')
for row in results:
	print(row)

