import argparse, inspect

parse = argparse.ArgumentParser()
parse.add_argument("--verbosity", help="increase output verbosity") # py <filename.py> --verbosity <anyvalue>  
                                                                    # any value is required cause default will be None, so we dont get any error  
args = parse.parse_args()
print(args)
if args.verbosity:   # Namespace(verbosity='1') then, True
    print("Verbosity turned on")