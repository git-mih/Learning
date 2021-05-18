import sys
import urllib.parse
import webbrowser

def main(args):
    def quote(arg):
        if ' ' in arg:
            arg = '"%s"' % arg
        return urllib.parse.quote_plus(arg)

    query_string = '+'.join(quote(arg) for arg in args)
    url = urllib.parse.urljoin('https://www.google.com/search', '?q=' + query_string)
    webbrowser.open(url)

if __name__ == '__main__':
    main(sys.argv[1:])
