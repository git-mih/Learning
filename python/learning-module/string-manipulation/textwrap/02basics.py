import textwrap

sample_text = '''
The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
'''

dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50) # wrapping w/ fill()
wrapped += '\n\nSecond paragraph after a blank line.'

final = textwrap.indent(wrapped, '> ') # indenting the wrapped text with: >
print(final)

dedented_text = textwrap.dedent(sample_text).strip()
final = textwrap.fill(sample_text,
					  initial_indent='*',
					  subsequent_indent=' ' * 4,
					  width = 50)
print(final)

#____________________________________________________________________
original = textwrap.fill(textwrap.dedent(sample_text), width=50)

print('\noriginal:\n')
print(original)

shortened = textwrap.shorten(original, 100) # 
shortened_wrapped = textwrap.fill(shortened, width=50)
print('\nshortened:\n')
print(shortened_wrapped)

# The textwrap module can be used to format text for
# output in situations where pretty-printing [...]
