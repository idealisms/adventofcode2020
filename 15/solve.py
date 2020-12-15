inp = open('input').read()
lines = inp.strip().splitlines()
# lines = [int(n) for n in lines]
numbers = [int(n) for n in lines[0].split(',')]

seq = []
for i in range(2020):
  if i < len(numbers):
    seq.append(numbers[i])
  else:
    last = seq[-1]
    try:
      seq.append(list(reversed(seq[:-1])).index(last) + 1)
    except ValueError:
      seq.append(0)
      continue
print('part1:', seq[-1])

seen = {}
prev = 0
for i in range(30000000):
  if i % 1000000 == 0:
    print(i, len(seen))
  if i < len(numbers):
    seen[numbers[i]] = [i]
    prev = numbers[i]
  else:
    lst = seen[prev]

    nxt = 0
    if len(lst) >= 2:
      nxt = lst[-1] - lst[-2]

    prev = nxt
    seen.setdefault(nxt, []).append(i)
print('part2:', prev)