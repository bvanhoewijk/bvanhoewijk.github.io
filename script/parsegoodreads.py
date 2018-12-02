#!/usr/bin/env python
import xml.etree.ElementTree as ET
import sys
from html.parser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return "".join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def cleantext(data):
    if data != None:
        return data.strip()
    return ""


def getStars(rating):
    stars = ""
    if rating == 0:
        stars = "N/A"
    else:
        for i in range(0, rating):
            stars += '<span class="glyphicon glyphicon-star" aria-hidden="true"></span>'
    return stars


def main():
    goodreadsxml = sys.argv[1]

    root = ET.parse(goodreadsxml).getroot()
    # print(
    #     "<thead><tr><th /><th>Title</th><th>Author</th><th>My rating</th></tr></thead><tbody>"
    # )
    reviewsfh = open("_includes/goodreadsreviews.html", "w")
    bookindex = 0
    for item in root.iter("item"):
        bookindex = bookindex + 1
        title = cleantext(item.find("title").text)
        author = cleantext(item.find("author_name").text)
        rating = int(strip_tags(cleantext(item.find("user_rating").text)))
        # rating = 5
        img = cleantext(item.find("book_small_image_url").text)
        user_review = cleantext(item.find("user_review").text)
        book_description = cleantext(item.find("book_description").text)
        book_description = strip_tags(book_description)
        book_description = (book_description.encode('ascii', 'ignore')).decode("utf-8")

        if user_review != None:
            user_review = strip_tags(user_review)
        else:
            user_review = str(rating) + " stars"

        reviewsfh.write(
            '<tr class="accordion-toggle" data-toggle="collapse" data-target="#%s">'
            % ("book" + str(bookindex))
        )
        reviewsfh.write('<td><img src="%s"/></td>' % img)
        reviewsfh.write("<td>%s</td>" % title)
        reviewsfh.write("<td>%s</td>" % author)
        reviewsfh.write(
            '<td><a href="#" data-toggle="tooltip" data-placement="top" title="%s">'
            % user_review
        )
        reviewsfh.write(getStars(rating))
        reviewsfh.write("</td></tr>")
        
        reviewsfh.write(
            '<tr><td class="zeroPadding" colspan="5"><div id="%s" class="collapse">%s</div></tr>'
            % ("book" + str(bookindex), book_description)
        )

    reviewsfh.write("</tbody>")


if __name__ == "__main__":
    main()
