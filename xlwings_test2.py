import datetime, time
import xlwings as xw
import random
import os

file_name = 'xlwings_sample.xlsx' # Excelファイル名（作成しておく必要あり）
# file_name = os.path.join(os.path.dirname(__file__), file_name)
wb = xw.Book(file_name) # Excelファイルを開く
sheet = wb.sheets['Sheet1']	# シートを作成（選択）
sheet.clear() # シート内のデータと書式をクリア

header = ['日時', 'データ1', 'データ2', 'データ3', 'データ4', 'データ5']
sheet.range('A1').value = header # ヘッダを書き出し

for i in range(2,7):

    # とりあえずランダムな値を5個生成
    data = []
    for _ in range(5):
        data.append(random.randint(1000, 5000))

    # 先頭に時刻を追加
    data.insert(0, datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    sheet.range('A'+str(i)).value = data # Excelに書込み
    time.sleep(1)

wb.save()