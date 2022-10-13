# 5.5
# ans = 25 # 回答

# count = 0 # 失敗した回数
# while True:
#     # データ入力
#     while True:
#         data = int(input('データを入力してください：'))
#         if data < 1 or data > 50:
#             print('正しいデータを入力してください。')
#             continue
#         break

#     count += 1
#     if data == ans:
#         print('正解です。')
#         break
#     elif data < ans:
#         print("小さいです")
#     else:
#         print("大きいです")
    
# # 終了する前に回数を表示
# print(str(count) + "回で正解しました。")

scores = []
for i in range(5):
    score = input("点数を入力してください。")
    score = int(score)
    scores.append(score)
print(scores)