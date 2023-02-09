
# BOOK QUERY

#1 MILESTONE - To print author name and first publishing year of the book. For example - To kill a mockingbird

import requests
import json

# Taking input of book name from the user
book_name = input("Enter book Name: ")

# With the application site, https://openlibrary.org/developers/api
# Click for search to find the titile link
resp = requests.get(f"http://openlibrary.org/search.json?title={book_name}")
info = resp.json()
publishing_year = info['docs'][0]['first_publish_year']
author_name = info['docs'][0]['author_name'][0]

print(f"Author of '{book_name}' is {author_name}. It was first published in {publishing_year}")