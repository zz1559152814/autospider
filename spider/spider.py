# -*- coding: utf-8 -*-
import sys;reload(sys);sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup
import urllib2

URL               = ["http://kokkai.ndl.go.jp/SENTAKU/syugiin/mainb.html"]
# TAGS have two elements,one is the tag of object.
# The other one records object 's serial number in the list of content which have the tag same with object
TAGS              = [['html body center table tr td table tr td[class] a[target]',0]]
# FILES have two elements,one is the file path to record data.
# The other one add the sign which users need to annotate the object
FILES             = [['./textfile.txt','回数: ']] 

# tag:consists of three levels information [tag attribution attribution_value]
def parse(url,tags,files,autoTag=False):
    req           = urllib2.Request(url[0])
    response      = urllib2.urlopen(req)
    html_text     = response.read()
    for i in range(len(tags)): 
        file      = open(files[i][0],'a')
        soup      = BeautifulSoup(html_text,'lxml')
        if autoTag == False:
            cnts      = tags[i][1]      # the serial number of the object needed in right-tag-list 
            result    = soup.select(tags[i][0])[cnts].string
            file.write(files[i][1]+result)
            file.close()
        elif autoTag == True:
            results    = soup.select(tags[i][0])
            file.write(files[i][1]+'\n')
            for result in results:
                file.write(result.string+'\n')
            file.close()


if __name__ == "__main__":
    parse(URL,TAGS,FILES,True)