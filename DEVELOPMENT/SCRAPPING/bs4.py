from bs4 import BeautifulSoup as bs

soup = bs("<p>Some <b> Bad <i> HTML")

print(soup.prettify())
