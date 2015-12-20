"""Uses wikiminer api to extract wikipedia articles from a string"""
from lxml import etree
import urllib2
import sys


def main():
    url = "http://wikipedia-miner.cms.waikato.ac.nz/services/wikify"
    # sys is used instead of input() and print() to support both py2 and py3
    sys.stdout.write("Enter your string : ")
    string = "?source=" + "%20".join(sys.stdin.readline().split())
    doc = etree.parse(urllib2.urlopen(url + string))
    articles = dict()
    total = len(articles)
    for df in doc.xpath("//detectedTopic"):
        total += 1
        articles[total] = dict()
        for attrib in df.attrib:
            articles[total][attrib] = df.attrib[attrib]
    sys.stdout.write("\nTotal number of articles found in your text " +
                     "is {}.\n".format(total))
    for i, data in articles.items():
        sys.stdout.write(repr(i) + "\t" + data['title'] + "\t" +
                         "http://en.wikipedia.org/?curid=" + data['id'] + "\n")

if __name__ == "__main__":
    main()
