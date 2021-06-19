import csv

# reading csv file, defining csv dialect & skiping header
def parse_data(fname):
	with open(fname) as f:
		dialect = csv.Sniffer().sniff(f.read(2000)) # reading 2k lines to find pattern and define dialect
		f.seek(0) # stepback
		next(f) # skiping header
		yield from csv.reader(f, dialect=dialect)

# filtering
def filter_data(data, word): 
	for row in data:  # data = parse_data('cars.csv')
		if word in row[0]: # if 'Chrevrolet' in current data row, then yield it
			yield row

def pipeline(fname, *filter_words):
	data = parse_data(fname)
	for word in filter_words:
		data = filter_data(data, word) ###
	yield from data

results = pipeline('cars.csv', 'Chevrolet', 'Monte', 'Landau')

print('\nGENERIC PIPELINE: (Chevrolet, Monte, Landau)')
for row in results:
	print(row)

# for word in ('Chevrolet', 'Monte', 'Landau'):
# 	data1   = filter_data(parse_data('cars.csv'), 'Chevrolet')
# 	data2   = filter_data(data1, 'Monte')
# 	results = filter_data(data2, 'Landau')
# 	yield from results  -> yield filtered rows from 'cars.csv'

# if we dont yield from, it will yield the filter_data generator for us

