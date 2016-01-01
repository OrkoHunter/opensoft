from __future__ import print_function
from lxml import html
import urllib2

page = html.document_fromstring('\n'.join(
        urllib2.urlopen('http://cse.iitkgp.ac.in/faculty4.php').readlines()))
names = page.xpath('//font[1]/b/a/b/text()')
desig = page.xpath('//font[2]/b[1]/text()')
for i in range(len(names)):
    name = ' '.join(names[i].split())
    print(name, end=" "*(26-len(name)))
    print(" | " + desig[i])
