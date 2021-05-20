import argparse
parser = argparse.ArgumentParser() # instantiating the Parser object which contains all properties and methods we need to work with

# POSITIONAL ARGUMENTS
parser.add_argument("square", help="echo the string you use here", type=int) # "square" will be stored into Namespace object. By default the type is str

args = parser.parse_args() # Display the -h when specified or errors. 
                           # Namespace object which contains echo=int(10) now  Namespace(echo= 10 )

print(args.square) # accessing the Namespace object property called square
print(args.square**2)