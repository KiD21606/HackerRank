from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for item in attrs:
            print('->', item[0], '>', item[1])
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for item in attrs:
            print('->', item[0], '>', item[1])

parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
