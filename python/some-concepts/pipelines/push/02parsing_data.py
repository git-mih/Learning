import csv
import itertools

def read_file(fname):
	with open(fname) as f:
		dialect = csv.Sniffer().sniff(f.read(2000))
		f.seek(0)
		next(f)
		yield from csv.reader(f, dialect=dialect)

headers    = ('make', 'model', 'year', 'vin', 'color')
converters = (str, str, int, str, str)

def data_parser():
	data = read_file('car_data.csv')
	next(data)
	for row in data:
		parsed_row = [converter(item)
					  for converter, item in zip(converters, row)]
		yield parsed_row

print('\n>>> islice(data_parser(), 4)')
for row in itertools.islice(data_parser(), 4):
	print(row)

print('\n>>> using range(4)')
data = data_parser()
for _ in range(4):
	print(next(data))