import os

print(os.getcwd())

data = '日本語'

with open('日本語ファイル.csv', 'w') as f:
    # f.write('日本語,日本語,日本語')
    for i in range(3):
        f.write(data)
        f.write(',')

with open('日本語ファイル.csv', 'r') as f:
    s = f.read()
print(s)
