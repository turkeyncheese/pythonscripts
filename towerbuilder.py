def tower_builder(n_floors):
    out = []
    width = (n_floors * 2) - 1
    for x in range(1, 2 * n_floors, 2):
        asterisks = x * '*'
        line = asterisks.center(width)
        out.append(line)
    return out

#tests
print(tower_builder(3))
print(tower_builder(7))
print(tower_builder(19))
print(tower_builder(100))
