x = input().split()
y = map(int, x)
z = [i for i in y if y < 0]

print(z)