import csv

prefs_out = [['東京都', 13960000],
             ['愛知県', 7553000],
             ['大阪府', 8823000]]

with open('県人口.csv', 'w', newline='') as fout:
# with open('県人口.csv', 'w') as fout:
    csv_out = csv.writer(fout)
    csv_out.writerows(prefs_out)
