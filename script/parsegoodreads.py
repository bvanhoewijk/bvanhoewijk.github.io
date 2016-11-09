#!/usr/bin/env python
import xml.etree.ElementTree as ET
from HTMLParser import HTMLParser


root = ET.parse('read.xml').getroot()

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
  
def cleantext(data):
  if data != None:
    return data.encode('utf-8').strip()
  return data

print '<table>'
print '<tr><th /><th>Title</th><th>Author</th><th>Rating</th></tr>'
for item in root.iter('item'):
  title = cleantext(item.find('title').text)
  author = cleantext(item.find('author_name').text)
  rating = cleantext(item.find('user_rating').text)
  img = cleantext(item.find('book_small_image_url').text)
  user_review = cleantext(item.find('user_review').text)
  book_description = cleantext(item.find('book_description').text)

  book_description = strip_tags(book_description)
  if user_review != None: 
    user_review = strip_tags(user_review)

  print "<tr>"
  print "<td><a href=\"#\" data-toggle=\"tooltip\" data-placement=\"down\" title=\"%s\"><img src=\"%s\"/></td>" % (book_description, img)
  print "<td><a href=\"#\" data-toggle=\"tooltip\" data-placement=\"down\" title=\"%s\">%s</td>" % (book_description, title)
  print "<td>%s</td>" % author
      # <li><a href="#" data-toggle="tooltip" data-placement="top" title="Hooray!">Top</a></li>
  print "<td><a href=\"#\" data-toggle=\"tooltip\" data-placement=\"top\" title=\"%s\">%s</td>" % (user_review, rating)
  print "</tr>"


print '</table>'

