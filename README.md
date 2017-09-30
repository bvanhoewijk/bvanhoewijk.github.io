# [Start Bootstrap](http://startbootstrap.com/) - [Landing Page]()

http://stackoverflow.com/questions/28733425/adding-bootstrap-to-jekyll
http://blackrockdigital.github.io/startbootstrap-landing-page/

curl -X GET 'https://www.goodreads.com/review/list_rss/44432722?key=o8dp_fosIdWMH1OTpl3p3wPJTE0winUjZQVNGCb6lWra7qTh&shelf=read' > read.xml
python script/parsegoodreads.py read.xml > table.html
