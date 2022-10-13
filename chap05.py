# i = list(range(10))
# print(i)

# i1 = list(range(10, 20))
# print(i1)

# i2 = list(range(1, 10, 2))
# print(i2)

# a = [5, 1, 3, 4]
# for i in range(len(a)):
#     print(i, a[i])

# a = [5, 1, 3, 4]
# for d in a:
#     print(d)

a = [5, 1, 3, 4]
for i, d in enumerate(a):
    print(i, d)

# a = [5, 1, 3, 4]
# sum = 0
# for i in range(len(a)):
#     sum += a[i]
# average = sum/len(a)
# print(average)

# a = [5, 1, 3, 4]
# sum = 0
# for i, d in enumerate(a):
#     sum += d
# average = sum/len(a)
# print(average)

# kita = ['茨城県', '栃木県', '群馬県', '福島県'] # リスト（配列もどき？）
# for i in range(len(kita)):
#     print(kita[i])

# kita = ['茨城県', '栃木県', '群馬県', '福島県'] # リスト（配列もどき？）
# for d in kita:
#     print(d)

# a = []
# for i in range(5):
#     a.append(i*i)
# print(a)

# a = [i*i for i in range(5)] # リスト内包表記
# print(a)

# if 'a' in 'abc' and 'b' in 'abc':
#     print('aが含まれています。')
# else:
#     print('aが含まれていません。')

# && → and
# || → or
# ! → not

# c = 2.99792458E8 # 3×1000000000
# na = 6.02214076E23
# # print('光速は{0:12.8g}m/s'.format(c))
# print('光速は{0:12.8g}m/s'.format(c))

# h = 170
# w = 53
# bmi = 53/(h/100*h/100)
# # TODO: 「身長170㎝、体重53kgのBMIは〇〇.〇です。」
# print('身長{0:}㎝、体重{1:}kgのBMIは{2:.1f}です。'.format(h, w, bmi))