n = int(input())
a = list(map(int, input().split()))
x = sum([1 / b for b in a])
print(1 / x)
