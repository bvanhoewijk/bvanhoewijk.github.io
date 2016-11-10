#!/usr/bin/env python
import xml.etree.ElementTree as ET
import sys
from HTMLParser import HTMLParser


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

def getStars(rating):
    stars = ""
    if int(rating) == 0:
        stars = "N/A"
    else:
        for i in range(0, int(rating)):
            stars += '<span class="glyphicon glyphicon-star" aria-hidden="true"></span>'
    return stars


def main():
    goodreadsxml = sys.argv[1]

    root = ET.parse(goodreadsxml).getroot()
    print '<thead><tr><th /><th>Title</th><th>Author</th><th>My rating</th></tr></thead><tbody>'

    bookindex = 0
    for item in root.iter('item'):
        bookindex = bookindex + 1
        title = cleantext(item.find('title').text)
        author = cleantext(item.find('author_name').text)
        rating = cleantext(item.find('user_rating').text)
        img = cleantext(item.find('book_small_image_url').text)
        user_review = cleantext(item.find('user_review').text)
        book_description = cleantext(item.find('book_description').text)

        book_description = strip_tags(book_description)
        if user_review != None: 
            user_review = strip_tags(user_review)
        else:
            user_review = str(rating) + " stars"

        print '<tr class="accordion-toggle" data-toggle="collapse" data-target="#%s">' % ("book" + str(bookindex))
        print '<td><img src="%s"/></td>' % img
        print '<td>%s</td>' % title
        print '<td>%s</td>' % author
        print '<td><a href="#" data-toggle="tooltip" data-placement="top" title="%s">' % user_review
        print getStars(rating)
        print '</td></tr>'
        print '<tr><td class="zeroPadding" colspan="4"><div id="%s" class="collapse">%s</div></tr>' % ("book" + str(bookindex), book_description)    

    print '</tbody>'

if __name__ == "__main__":
    main()