# -*- coding: utf-8 -*-
import sys;reload(sys);sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup
import urllib2

URL               = ["http://kokkai.ndl.go.jp/SENTAKU/syugiin/mainb.html"]
TAGS              = ['html body center table tr td table tr td[class] a[target]']
FILES             = [['./textfile.txt','回']] 
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# tag:consists of three levels information [tag attribution attribution_value]
def parse(url,tags,files):
    req           = urllib2.Request(url[0])
    response      = urllib2.urlopen(req)
    html_text     = response.read()
    # print html_text
    soup = BeautifulSoup(html_text,'lxml')
    print soup.prettify()
    results = soup.select(tags[0])
    for result in results:
        print type(result)
        print result.name
        print result.attrs
        print type(result.attrs)
        print result.string
        print result.contents
        print type(result.string)
parse(URL,TAGS,FILES)