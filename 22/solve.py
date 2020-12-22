import collections
import itertools

inp = open('input').read()
tinp = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''
p1_lines, p2_lines = inp.strip().split('\n\n')
p1 = [int(n) for n in p1_lines.split('\n')[1:]]
p2 = [int(n) for n in p2_lines.split('\n')[1:]]

while len(p1) > 0 and len(p2) > 0:
  if p1[0] > p2[0]:
    p1 = p1[1:] + [p1[0], p2[0]]
    p2 = p2[1:]
  else:
    p2 = p2[1:] + [p2[0], p1[0]]
    p1 = p1[1:]

win = p1 if len(p1) > 0 else p2
print('part1:', sum((i+1) * v for i, v in enumerate(reversed(win))))

def combat(p1, p2):
  if len(p1) == 0 or len(p2) == 0:
    return p1, p2

  if p1[0] > len(p1) - 1 or p2[0] > len(p2) - 1:
    if p1[0] > p2[0]:
      p1 = p1[1:] + [p1[0], p2[0]]
      p2 = p2[1:]
    else:
      p2 = p2[1:] + [p2[0], p1[0]]
      p1 = p1[1:]

    return p1, p2

  p1s, p2s = p1[1:1+p1[0]], p2[1:1+p2[0]]
  mem = set()
  while len(p1s) > 0 and len(p2s) > 0:
    key = (tuple(p1s), tuple(p2s))
    if key in mem:
      p1s, p2s = [1], []
      break
    mem.add(key)
    p1s, p2s = combat(p1s, p2s)

  if len(p1s) > 0:
    p1 = p1[1:] + [p1[0], p2[0]]
    p2 = p2[1:]
  else:
    p2 = p2[1:] + [p2[0], p1[0]]
    p1 = p1[1:]

  return p1, p2

p1 = [int(n) for n in p1_lines.split('\n')[1:]]
p2 = [int(n) for n in p2_lines.split('\n')[1:]]
while len(p1) > 0 and len(p2) > 0:
  p1, p2 = combat(p1, p2)

print(p1, p2)
win = p1 if len(p1) > 0 else p2
print('part2:', sum((i+1) * v for i, v in enumerate(reversed(win))))
