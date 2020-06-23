
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


print(f"There are {len(entries)} entries")

for entry in entries:
    # import pdb; pdb.set_trace()
    print(entry.find('article:title', ns).text)