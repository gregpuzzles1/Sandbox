import urllib.request
import csv

url = "http://www.cs.columbia.edu/~joshua/teaching/cs3101/simpsons_diet.csv"

list_string = []

# Open the URL and read the CSV content
with urllib.request.urlopen(url) as response:
    lines = [line.decode('utf-8') for line in response.readlines()]
    reader = csv.reader(lines, delimiter=',', quotechar='"')

    for char, meal, ate, qty, com in reader:
        if char != 'Character':  # Skip header row
            list_string.append(f"{char} {meal} {ate} {qty} {com}")

# Print the resulting list
print(list_string)
