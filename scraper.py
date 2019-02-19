# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# line 4 is importing a library for line 3
import scraperwiki
import lxml.html
## Import defines the content to be scraped
#
print("hello")
# # Read in a page
html = scraperwiki.scrape("http://foo.com")
## html is a variable
## Content in the brackets is a string
print (html)
## Code fetches data from foo.com
## print allows the scraper to fetch and print the code from the string

# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
print (root.cssselect("a"))
## 'Root' is creating a new variable
## lxml.html is a library that we imported earlier
## (html) is the entire contents of the webpage we already scraped
## div is a html tag
## cssselect is a function bc it's followed by a bracket


listofmatches = root.cssselect("a")
for match in listofmatches:
       print (match)
       lxml.html.twostring(match)

print (root)

       

# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
