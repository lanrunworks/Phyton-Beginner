a = [5, 1, 3, 4]
print(a)
print(a[0])
print(a[2])

b = ['三条', '四条', '五条', '七条']
c = 5
a = [c, 1, 3, 4]

a = [1] * 4
a

e =list()
e = []
n = range(5)
n
n = list(n)
print(n)

s = list('abcde')
s = list('茨城県')
print(s)

t = 'a textbook of Python'
tlist = t.split()
print(tlist)

tlist = 'a textbook of Python'.split()
print(tlist)

print(len(a))
print(len('茨城県'))

a = [5, 1, 3, 4]
print(a[-5])

b = a[1:3]
print(b)

# 練習問題
# 4.4 リストの生成
list_i = [1, 3, 5, 7, 9]
list_str = ['Tokyo', 'Nagoya', 'Osaka']

list_tree_major = [1, 'Tokyo', 2, 'Osaka', 3, 'Nagoay']

list_score = list(range(100))
print(list_score)

list_zen_of_python = 'Simple is better than complex.'.split()

# 4.6 リストの要素へのアクセス
i = list(range(1,11))
print(i[3])
print(i[5])

i[3] = i[5] = 0
print(i)

i = list(range(51))
length = len(i)
i[length-2] = 0
print(i)

# 4.7 負の添え字とスライス
i = list(range(1, 11))
i[-2] = 0
print(i)
i[-11] = 0
print(i)

i = list(range(1, 11))
first = i[:2]
last = i[len(i)-2:]
print(i)
print(first)
print(last)

i = list(range(101))
center = len(i)//2
first = i[:center]
last = i[center:]
print(first)
print(last)

i = list(range(101))
center = len(i)//2
first = i[center-5:center]
last = i[center:center+5]
print(first)
print(last)
