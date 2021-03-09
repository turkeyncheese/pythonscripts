import sys
x = int(sys.argv[1])
a, b = 0, 1

if x == 0:
    print(a)
elif x == 1:
    print(b)
else:
    for i in range(2,x):
        a, b = b, a + b
print(a)
