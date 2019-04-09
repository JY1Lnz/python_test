import math

fenzi = 1.43e-14
e = 1.60e-19


def Get_q(data, u):
    res = []
    sum = 0.0
    for value in data:
        fenmu = float(math.sqrt((value * (1 + 0.02 * math.sqrt(value))) ** 3) * u)
        sum += fenzi / fenmu
        res.append(fenzi / fenmu / e)
    n = int(sum / len(data) / e)
    q = sum / len(data)
    re = q / n
    return res, n, q, re


def Get_Q_Average(data):
    sum = 0.0
    for value in data:
        sum += value
    return sum / len(data)

