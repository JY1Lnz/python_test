import physical2

fenzi = 1.43e-14

data1 = [5.80, 5.56, 5.56, 5.57, 5.55]
data2 = [13.18, 12.59, 13.31, 13.14, 12.94]
u1 = 38
u2 = 78
res1, n1, q1, e1 = physical2.Get_q(data1, u1)
print(res1, n1, q1, e1 / physical2.e)
print(e1)

res2, n2, q2, e2 = physical2.Get_q(data2, u2)

print(res2, n2, q2, e2 / physical2.e)
print(e2)
print((e1+e2)/2)
print((e1 + e2) / physical2.e / 2)
