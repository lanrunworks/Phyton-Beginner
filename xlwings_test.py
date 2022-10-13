import xlwings as xw
wb = xw.Book('xlwings_sample.xlsx')  # Excelファイルを開く
sheet = wb.sheets['Sheet1']  # シートを作成（選択）
sheet.range('A1').value = '1000'  # A1セルに値を書き込み
print(sheet.range('A1'))  # A1セルの値を読み出し

# A2:D3セルにリストを書き込み
sheet.range('A2').value = [['1000', '2000', '3000'], [1000, 2000, 3000]]
print(sheet.range('A2').expand().value)  # A2:D3セルのデータを読み出し
wb.save()  # ファイルを上書き保存
wb.close()  # Excelを閉じる
