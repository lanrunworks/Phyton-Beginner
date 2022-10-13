import csv
from xml.etree.ElementPath import prepare_self

prefs = []
with open('県人口.csv', 'r') as fin:
    csv_in = csv.reader(fin)
    for row in csv_in:
        prefs.append(row)
print(prefs)