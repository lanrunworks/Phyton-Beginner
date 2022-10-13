# #Random
# import random
# num = random.randint(10, 100)
# print(num)

# #screensize
# import turtle
# turtle.home() # とりあえずTurtle用スクリーンを表示
# size = turtle.screensize() # スクリーンサイズを取得
# print(size)
# turtle.done() # 終了

# #円
# import turtle
# turtle.color('black') # 線の色を黒に設定
# speed = turtle.speed('fastest') # 描画スピードを最速に設定
# turtle.circle(100) # 半径100の円を描画
# turtle.speed(speed) # 描画スピードを元に戻す
# turtle.done()

# #redcircle
# import turtle
# turtle.color('black', 'red') # 線の色と塗りつぶしの色を黒に設定
# speed = turtle.speed('fastest')
# turtle.begin_fill() # 塗りつぶしを開始
# turtle.circle(100)
# turtle.end_fill() # 塗りつぶしを終了
# turtle.speed(speed)
# turtle.done()

# #click
# import turtle
# def hello(x, y):
#     """マウスクリックで呼び出される関数（イベントハンドラ）"""
#     print(f'座標({x},{y})でクリックされました。')
# turtle.home()
# turtle.onscreenclick(hello) # スクリーンをクリックしたときに呼び出される関数を設定
# turtle.done()

# #clickerase
# import turtle
# def screen_clear(x, y):
#     turtle.clear() # スクリーンをクリア
# turtle.speed('fastest')
# turtle.color('blue', 'blue')
# turtle.begin_fill()
# turtle.circle(100)
# turtle.end_fill()
# turtle.speed('normal')
# turtle.onscreenclick(screen_clear) # スクリーンをクリックしたときに呼び出される関数を設定
# turtle.done()

# app

import turtle

turtle.home()
size = turtle.screensize()
print(size)
turtle.done()