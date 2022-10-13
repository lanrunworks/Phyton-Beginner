# #1
# def sum_list(data):
#     return sum(data)

# sum = sum_list([1, 2, 3, 4, 5])
# print(sum)


# #2
# def calc_bmi(height, weight):
#     return weight / (height/100 * height/100)

# def print_bmi(bmi):
#     if bmi < 18.5:
#         print('低体重')
#     elif bmi < 25:
#         print('普通体重')
#     elif bmi < 30:
#         print('肥満（1度）')
#     elif bmi < 35:
#         print('肥満（2度）')
#     elif bmi < 40:
#         print('肥満（3度）')
#     else:
#         print('肥満（4度）')

# bmi = calc_bmi(170, 80)
# print_bmi(bmi)

# #3
# def double_list(data):
#     for i in range(len(data)):
#         data[i] *= 2
#     return data
#     # return [ x * 2 for x in data]

# print(double_list([1, 2, 3, 4, 5]))

# # 4
# def get_area(data, f):
#     a = data["bottom"]
#     b = data["height"]
#     return f(a, b)


# def triangle(bottom, height):
#     return bottom*height/2


# print(get_area({'bottom': 100, 'height': 150}, triangle))

# # 5
# from cmath import pi


# def get_area(data, f):
#     c = data["radius"]
#     return f(c)


# def circle(data):
#     return data*data*pi


# print(get_area({'radius': 150}, circle))

# 6
def print_list(data):
    str = []
    for i in range(len(data)):
        for j in range (len(data[i])):
            str.append(data[i][j])
    return print(str)

print_list([1, 2, [3, 4, 5], 6, 7, [8, 9], 10])
