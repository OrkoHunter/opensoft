from lxml import etree
import urllib2
import sys

def main():
    url = "http://wikipedia-miner.cms.waikato.ac.nz/services/wikify"
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
        sys.stdout.write(repr(i) + "\t" + data['title'] + "\n")

if __name__ == "__main__":
    main()
