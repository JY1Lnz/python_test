import math

frequency = [8.214e14, 7.408e14, 6.879e14, 5.490e14, 5.196e14]
e = 1.60e-19

data = [1.838, 1.616, 1.310, 0.706, 0.588]


def Get_K(data):
    k = []
    for i in range(0, 4):
        fenmu = frequency[i] - frequency[i+1]
        fenzi = data[i] - data[i+1]
        k.append(fenzi/fenmu)
    sum = 0
    for value in k:
        sum += value
    return k, sum/len(k)


k, average = Get_K(data)
h = e*average
print(k, average, h)
