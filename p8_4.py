# from turtle import * # turtleモジュールからすべて読み込み

# def come(x, y): # 関数の定義
#     (xx, yy) = pos() # 現在位置の取得
#     newxy = ((xx+x)/2, (yy+y)/2) # 新しい位置の生成
#     # newxy = ((xx+x), (yy+y)) # 新しい位置の生成
#     print(x, y) # コンソールに表示
#     goto(newxy) # 新しい位置に移動

# onscreenclick(come) # クリックで呼び出す関数を設定
# done() # Turtleグラフィックスを終了

# こちらのほうがわかりやすいかも… 入力する量は多いですが…
import turtle # turtleモジュールからすべて読み込み

def come(x, y): # 関数の定義（xとyはマウスをクリックした位置）
    (xx, yy) = turtle.pos() # 前の位置の取得
    # newxy = ((xx+x)/2, (yy+y)/2) # 新しい位置の生成
    newxy = (x, y) # 新しい位置の生成
    print(x, y) # コンソールに表示
    turtle.goto(newxy) # 新しい位置に移動

turtle.onscreenclick(come) # クリックで呼び出す関数を設定
turtle.done() # Turtleグラフィックスを終了
