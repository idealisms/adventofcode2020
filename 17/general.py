'''A solution for any number of dimensions or steps.'''
import itertools

inp = open('input').read()
lines = inp.strip().splitlines()

def gen_adjacent(pt):
  '''Generator of points adjacent to pt.'''
  dimensions = len(pt)
  ranges = [(-1, 0, 1) for _ in range(dimensions)]
  for deltas in itertools.product(*ranges):
    if deltas.count(0) == len(deltas):
      continue
    yield tuple(a + b for a, b in zip(pt, deltas))

def step(dimensions, active):
  new_active = set()
  pts_to_test = set()
  for pt in active:
    pts_to_test.add(pt)
    for adj_pt in gen_adjacent(pt):
      pts_to_test.add(adj_pt)

  for test_pt in pts_to_test:
    adj_active_cnt = 0
    for adj_pt in gen_adjacent(test_pt):
      if adj_pt in active:
        adj_active_cnt += 1

    if test_pt in active and adj_active_cnt in (2, 3):
      new_active.add(test_pt)
    elif test_pt not in active and adj_active_cnt == 3:
      new_active.add(test_pt)

  return new_active

def solve(dimensions, steps):
  active = set()

  # Initialize the board.
  for x, line in enumerate(lines):
    for y, c in enumerate(line):
      if c == '#':
        active.add((0,) * (dimensions - 2) + (x, y))

  for _ in range(steps):
    active = step(dimensions, active)

  return len(active)

print(solve(3, 6))
print(solve(4, 6))
