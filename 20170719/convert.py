import csv
import json

csvfile = open('config.txt', 'r')
jsonfile = open('config.json', 'w')

reader = csv.DictReader(csvfile)
for row in reader:
	json.dump(row, jsonfile)
	jsonfile.write('\n')
