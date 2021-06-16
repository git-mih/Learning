import textwrap

sample_text = '''
The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''

print(textwrap.fill(sample_text, width=50))

print()

dedented_text = textwrap.dedent(sample_text) # opposite of "indented"
print('dedented: ', dedented_text) # block of text

# combining both
dedented_text = textwrap.dedent(sample_text).strip()
for width in [45, 60]:
	print(f'{width} Columns:')
	print(textwrap.fill(dedented_text, width=width))
	print()