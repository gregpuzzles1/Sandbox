import urllib
import csv
url = r"http://www.cs.columbia.edu/~joshua/teaching/cs3101/simpsons_diet.csv"
simpsons = urllib.urlopen(url)
reader = csv.reader(simpsons, delimiter=',', quotechar='"')

list_string = []

for char, meal, ate, qty, com in reader:
    if char != 'Character':
        list_string.append("%s %s %s %s %s" % (char, meal, ate, qty, com))

print list_string
