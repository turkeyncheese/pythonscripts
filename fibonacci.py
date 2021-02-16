import sys
x = int(sys.argv[1])
n1 = 0
n2 = 1

if x == 0:
    print(n1)
elif x == 1:
    print(n2)
else:
    for i in range(2,x):
        n3 = n1 + n2 
        n1 = n2 
        n2 = n3

print(n3)
