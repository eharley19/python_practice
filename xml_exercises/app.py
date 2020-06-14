import requests
import xml.etree.ElementTree as ET
from pprint import pprint

import turtle

r = requests.get('https://raw.githubusercontent.com/shawnbanasick/easy-htmlq/master/settings/statements.xml')

# pprint(dir(r))
# print(r.raw)
root = ET.fromstring(r.text)
statements = root.findall('statement')

for statement in statements:
    print(statement.text)

# s = turtle.getscreen()

# print(r.text)