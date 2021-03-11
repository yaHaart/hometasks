from bs4 import BeautifulSoup

with open("site.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print(soup.meta)
