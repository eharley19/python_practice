import xml.etree.ElementTree as ET
from pprint import pprint

tree = ET.parse('c:/Users/eharl/OneDrive/Documents/sample.xml')

root = tree.getroot()

books = root.findall('book')

for book in books:
    print(book[0].atext)
    print(book[1].text)
