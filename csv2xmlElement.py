import csv
from xml.etree.ElementTree import ( Element,
                                    tostring,
                                    )
import argparse
from pathlib import Path

def toXmlFile():
    with open(csvPathname, 'rt') as r, open(xmlPathname, 'wb') as w:
        rows = csv.DictReader(r)
        for row in rows:
            root = Element(xmlElementName)
            for k, v in row.items():
                if not v or k in csvIgnoring :
                    continue 
                root.set(k,v)
            w.write(tostring(root, short_empty_elements=True))
            w.write(b'\n')

def main():
    # Get arguments
    global csvPathname, xmlPathname, xmlElementName, csvIgnoring
    parser = argparse.ArgumentParser(description='import csv file to xml empty content element with attributes')
    parser.add_argument('--csv', type=str, required=True, help='csv file pathname')
    parser.add_argument('--xml', type=str, required=True, help='xml file pathname')
    parser.add_argument('--element', type=str, required=False, help='xml element name; default will be csv file name')
    parser.add_argument('--ignoring', type=str, required=False, help='csv key which will be ignored')

    args = parser.parse_args()
    csvPathname = args.csv
    xmlPathname = args.xml
    xmlElementName = args.element if args.element else Path(csvPathname).stem
    csvIgnoring = list(args.ignoring.split(',')) if args.ignoring else []
    
    toXmlFile()
main()
