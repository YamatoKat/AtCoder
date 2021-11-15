X = int(input()) / 1000

if X < 0.1:
    print("00")
elif 0.1 <= X <= 5:
    print("{0:02d}".format(int(X * 10)))
elif 6 <= X <= 30:
    print(int(X + 50))
elif 35 <= X <= 70:
    print(int((X - 30) / 5 + 80))
elif 70 < X:
    print(89)
