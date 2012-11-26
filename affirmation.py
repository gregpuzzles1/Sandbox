from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import re

webpage = urlopen('http://www.mustardseed7.org/obstacles_and_incentives_to_faith.html').read()

#patFinderAffirm = re.compile('(<p><em>)AFFIRMATION.*</p>')
patFinderAffirm = re.compile('<p><em>')

patFinderLink = re.compile('<a href="(.*)">')
#patFinderLink = re.compile('<a')

findPatAffirm = re.findall(patFinderAffirm, webpage)
findPatLink = re.findall(patFinderLink, webpage)

listIterator = []
listIterator[:] = range(1,len(findPatAffirm))

for i in listIterator:
    print findPatAffirm[i]
    #print findPatLink[i]

        


def main():
  pass

if __name__ == '__main__':
  main()
