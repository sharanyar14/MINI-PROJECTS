
# BOOK QUERY

#2 MILESTONE - To print common subjects in books

import requests
import json
book1 = "Lord of the flies"
book2 = "Animal Farm"
resp1 = requests.get(f"http://openlibrary.org/search.json?title={book1}")
resp2 = requests.get(f"http://openlibrary.org/search.json?title={book2}")
info1 = resp1.json()
info2 = resp2.json()
subj1 = info1['docs'][0]['subject']
subj2 = info2['docs'][0]['subject']
common = set(subj1) & set(subj2)
common = list(common)
print("Common subjects are:", common)