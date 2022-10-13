x = 2
rnew = x
diff = rnew - x/rnew # 2つの差を求める
if diff < 0: # 差が0より小さいときは正にする
    diff = -diff

while diff > 1.0E-6: # 差が0.000001より小さくなるまで繰り返し
    
    # 以下の3行で平方根の値（近似値）を計算
    r1 = rnew # 新しい値で更新
    r2 = x/r1
    rnew = (r1 + r2)/2 # 中間値を求める
    
    print(r1, rnew, r2)
    diff = r1 - r2 # 新しく計算した値と古い値の差を求める
    if diff < 0: # 差が0より小さいときは正にする
        diff = -diff