import csv

# ファイルを開く
try:
    with open('県人口.csv', 'r') as fin:
        csv_in = csv.reader(fin)

        # ファイルからデータを読み出す
        prefs = []
        for row in csv_in:
            prefs.append(row)
except FileNotFoundError:
    print('ファイルがありません。')
    exit()

# データ表示する
print(prefs)

# 人口の合計を求める
# print(int(prefs[0][1]) + int(prefs[1][1]) + int(prefs[2][1]))
sum = 0
for i in range(len(prefs)):
    sum += int(prefs[i][1])
print(sum)

# 日本の人口における割合を表示（125800000）
print(f'三大都市の日本の人口に占める割り合いは{sum/125800000*100:.2F}です。')
