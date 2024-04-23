def testclass(x, y): #関数
    print('平均を計算')
    n = (x + y) / 2
    s = y - x
    return n, s
a, b = testclass(10, 12)
print(a)
print(b)