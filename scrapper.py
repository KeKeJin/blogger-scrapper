import requests
from bs4 import BeautifulSoup
from pylatex import Document, Section, Subsection
import os

URL = "http://hayase.blogspot.com/2004/10/shadow-our-black-mutt.html"
page = requests.get(URL)

title = "post-title entry-title"

body = "post-body entry-content"

time = "published"

date = "date-header"

comments = "comments-content comment"

commentUser = "user"

commentContent = "comment-content"

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id = "outer-wrapper")

i_title_container = results.find("h3", {"class": title})
# i_title = i_title_container.find("a").text

i_content_container = results.find("div", {"class": body})
# i_content = i_content_container.find_all("span")
# print(i_title_container.text)
# print(i_content_container)
# for i in i_content:
#     print (i.text)

doc = Document()
with doc.create(Section('The simple stuff')):
    doc.append(i_content_container.text)

doc.generate_pdf()
