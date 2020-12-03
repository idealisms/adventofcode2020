inp = open('input').read()
lines = [x for x in inp.strip().split('\n') if x != '']

x = -3
trees = 0
for line in lines:
  x += 3
  if line[x % len(line)] == '#':
    trees += 1

print(trees)

def calc(dx, dy):
  x = -dx
  y = -dy
  trees = 0
  while True:
    x += dx
    y += dy
    if y >= len(lines):
      return trees
    line = lines[y]
    if line[x % len(line)] == '#':
      trees += 1

print(calc(1, 1) * calc(3, 1) * calc(5, 1) * calc(7, 1) * calc(1, 2))

