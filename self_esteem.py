from operator import index


num = [1,2,3,4,5,6,7,8,2,3,4,5,56,7]

lst = num[0::2]
print(sorted(lst))


a = True
sum = 0
while a:
    x = float(input())
    if x > 0:
        sum += x
    else:
        a = False

print(sum)
