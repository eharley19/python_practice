
import requests
import xml.etree.ElementTree as ET
from pprint import pprint

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'})

data = session.get('https://www.reddit.com/r/NHKEasyNews/.rss')

# pprint(data.text)

# namespace dictionary
ns = {'article': 'http://www.w3.org/2005/Atom'}

root = ET.fromstring(data.text)
entries = root.findall('article:entry', ns)
# import pdb; pdb.set_trace()

b = ''

print(f"There are {len(entries)} entries")

for entry in entries:
    # import pdb; pdb.set_trace()
    b += f"<p><a href='{entry.find('article:link', ns).attrib['href']}'>{entry.find('article:title', ns).text}</a></p>"

a = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
    <body>
    {b}
    </body>
</html>
"""


print(a)