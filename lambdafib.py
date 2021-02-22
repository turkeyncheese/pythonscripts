f = lambda a, b: (a lambda: f(b, a + b))
g = f(0, 1)

n = int(input('What term?: '))

for i in range(1, n):
  g = g[1]()
print(g[0])
