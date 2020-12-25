import collections
import itertools

inp = open('input').read()
dkey, ckey = list(map(int, inp.strip().splitlines()))

sn = 7
value = 1
loop_size = None
for_value = None
for i in range(100000000):
  value = (value * sn) % 20201227
  if value in (dkey, ckey):
    loop_size = i + 1
    for_value = value
    break

sn = dkey if for_value == ckey else ckey
value = 1
for _ in range(loop_size):
  value = (value * sn) % 20201227
print('part1:', value)
