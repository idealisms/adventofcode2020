import collections
import itertools

inp = open('input').read()
lines = inp.strip().splitlines()

def calc_point(line):
  pt = [0, 0]
  # odd-r https://www.redblobgames.com/grids/hexagons/
  # Thanks amitp!
  while len(line):
    if line.startswith('e'):
      pt[0] += 1
      line = line[1:]
    elif line.startswith('w'):
      pt[0] -= 1
      line = line[1:]
    elif line.startswith('sw'):
      if pt[1] % 2 == 0:
        pt[0] -= 1
      pt[1] += 1
      line = line[2:]
    elif line.startswith('se'):
      if pt[1] % 2 == 1:
        pt[0] += 1
      pt[1] += 1
      line = line[2:]
    elif line.startswith('nw'):
      if pt[1] % 2 == 0:
        pt[0] -= 1
      pt[1] -= 1
      line = line[2:]
    elif line.startswith('ne'):
      if pt[1] % 2 == 1:
        pt[0] += 1
      pt[1] -= 1
      line = line[2:]
  return tuple(pt)

WHITE, BLACK = 0, 1
pts = collections.defaultdict(int)
for line in lines:
  pt = calc_point(line)
  pts[pt] = (pts[pt] + 1) % 2
print('part1:', sum(n for n in pts.values()))

def get_adj(pt):
  return [
      (pt[0] + 1, pt[1]),  # e
      (pt[0] - 1, pt[1]),  # w
      (pt[0] - 1 if pt[1] % 2 == 0 else pt[0], pt[1] + 1),  # sw
      (pt[0] + 1 if pt[1] % 2 == 1 else pt[0], pt[1] + 1),  # se
      (pt[0] - 1 if pt[1] % 2 == 0 else pt[0], pt[1] - 1),  # nw
      (pt[0] + 1 if pt[1] % 2 == 1 else pt[0], pt[1] - 1),  # ne
  ]

def step(black):
  consider = set(black)
  for pt in black:
    for adj in get_adj(pt):
      consider.add(adj)

  new_black = set()
  for pt in consider:
    is_black = pt in black

    adj_black = 0
    for adj in get_adj(pt):
      if adj in black:
        adj_black += 1

    if is_black and adj_black in (1, 2):
      new_black.add(pt)
    elif not is_black and adj_black == 2:
      new_black.add(pt)
  return new_black

black = set(pt for pt, color in pts.items() if color == BLACK)
for _ in range(100):
  black = step(black)

print('part2:', len(black))
