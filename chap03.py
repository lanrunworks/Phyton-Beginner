# a = 1
# b = 2
# tmp = a # aの値を一時退避
# a = b # aの値をbで上書き
# b = tmp # bの値をtmp（実際は最初のaの中身）で上書き
# print(a, b)

# a = 1
# b = 2
# a, b = b, a # 値の入れ替え
# print(a, b)

# a = 1
# b = 1.0
# c = 10/2
# d = 10//2 # 結果が必ず整数
# e = '1'
# f = "1.0"
# print(type(a), type(b), type(c),
#       type(d), type(e), type(f))

# a = 'Tokyo'
# b = 'Osaka'
# a, b = b, a
# print(a, b)

# a = 'Tokyo'
# b = 'Osaka'
# tmp = a
# a = b
# b = tmp
# print(a, b)

# bottom = 10
# height = 5
# area = bottom * height / 2
# print('底辺:', bottom)
# print('高さ:', height)
# print('面積:', area)

pc = 50000
monitor = 20000
mouse = 2000
pad = 1000
sum = pc + monitor + mouse + pad
tax = sum * 0.1
print('消費税:', tax)