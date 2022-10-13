x = 2
rnew = x
rnew_list = [rnew]

r1 = rnew
r2 = x/r1
rnew = (r1+r2)/2 # 2の平方根を求める公式に当てはめる
# rnew = (r1+2/r1)/2
print(r1, rnew, r2)
rnew_list.append(rnew)

r1 = rnew
r2 = x/r1
rnew = (r1+r2)/2 # 2の平方根を求める公式に当てはめる
print(r1, rnew, r2)
rnew_list.append(rnew)

r1 = rnew
r2 = x/r1
rnew = (r1+r2)/2 # 2の平方根を求める公式に当てはめる
print(r1, rnew, r2)
rnew_list.append(rnew)

r1 = rnew
r2 = x/r1
rnew = (r1+r2)/2 # 2の平方根を求める公式に当てはめる
print(r1, rnew, r2)
rnew_list.append(rnew)
print(rnew_list)