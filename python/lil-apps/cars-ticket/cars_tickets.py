from collections import namedtuple, defaultdict
from datetime import datetime
from functools import partial

file_name = 'details.csv' 

with open(file_name) as f:
    column_headers = next(f).strip('\n').split(',')

column_names = [header.replace(' ', '_') 
                for header in column_headers]

Ticket = namedtuple('Ticket', column_names)


def parse_int(value, default=None):
    try:
        return int(value)
    except ValueError:
        return default

def parse_date(value, default=None):
    date_format = '%d/%m/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default

def parse_str(value, default=None):
    try:
        cleaned = value.strip()
        if not cleaned: # empty str
            return default
        else:
            return cleaned
    except ValueError:
        return default

column_parsers = (parse_int,
                  parse_str,
                  partial(parse_str, default=''),
                  partial(parse_str, default=''),
                  parse_date,
                  parse_int,
                  partial(parse_str, default=''),
                  parse_str,
                  lambda x: parse_str(x, default='')
                 )

def read_data():
    with open(file_name) as f:
        next(f)
        yield from f

def parse_row(row, default=None):
    fields = row.strip('\n').split(',')
    # fields = ['4006478550', 'VAD7274', 'VA', 'PAS', '10/5/2016', '5', '4D', 'BMW', 'BUS LANE VIOLATION']
    parsed_data = [fn(field) # (parse_int(field)), (parse_str(field)), ... 
                   for fn, field in zip(column_parsers, fields)] 
    # parsed_data = [4006478550, 'VAD7274', 'VA', 'PAS', datetime.date(2016, 5, 10), 5, '4D', 'BMW', 'BUS LANE VIOLATION']
    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    else:
        return default

def parse_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed

def violation_count_by_make():
    make_counts = defaultdict(int)
    for data in parse_data():
        make_counts[data.vehicle_make] += 1

for ticket in parse_data():
    print(ticket, end='\n\n')

