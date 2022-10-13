import csv
with open('08IBARAK.csv') as fin:
    cin = csv.reader(fin)
    data = [row for row in cin]
print(data)

for row in data:
    if row[6] == '茨城県' and row[7] == '常総市' and row[8] == '水海道高野町':
        print(row[2])
