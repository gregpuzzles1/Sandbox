from bs4 import BeautifulSoup
import requests
print "Success"

url = 'https://alphacentauri32.wordpress.com/2011/07/07/python-photo-mosaic/'.encode('utf-8')
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
print soup.prettify()
'''anchor = soup.find('table', attrs={'class': 'resultsTable'})

match = 'g-asm'
for a in soup.findAll('a'):
    if a.has_attr('class'):
        #if a['class'] == match: # and a['class'].match:
            #continue

    	print a['class'], a.contents

    if div.has_attid="itIn"'''