from pprint import pprint
from bs4 import BeautifulSoup
import gzip
print("DEBUG")
with gzip.open("/Users/eharl/Downloads/JMdict_e.gz", "rb") as f:
    file_content = f.read()
print("DEBUG")
soup = BeautifulSoup(file_content, "lxml")
print("Searching for entries...")
entries = soup.find_all("entry", limit=10)
for entry in entries:
    pprint(entry.get_text())