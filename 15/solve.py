inp = open('input').read()
lines = inp.strip().splitlines()
# lines = [int(n) for n in lines]
numbers = [int(n) for n in lines[0].split(',')]

# seq = []
# for i in range(2020):
#   if i < len(numbers):
#     seq.append(numbers[i])
#   else:
#     last = seq[-1]
#     try:
#       seq.append(list(reversed(seq[:-1])).index(last) + 1)
#     except ValueError:
#       seq.append(0)
#       continue
# print('part1:', seq[-1])

# Original solution used. Running times:
# time python3 (3.8.2):
#   real    0m42.112s
#   user    0m41.201s
#   sys     0m0.911s
# time pypy3:
#   real    0m10.752s
#   user    0m10.182s
#   sys     0m0.570s
seen = {}
prev = 0
for i in range(30000000):
  if i % 1000000 == 0:
    print(i)
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

# Attempt to speed up part 2, ~25-35% faster, but still slow.
# time python3 (3.8.2):
#   real    0m27.539s
#   user    0m27.249s
#   sys     0m0.290s
# time pypy3:
#   real    0m8.095s
#   user    0m7.794s
#   sys     0m0.300s
# size = 30000000
# seen = [None] * size
# prev = 0
# for i in range(size):
#   if i % 1000000 == 0:
#     print(i)
#   if i < len(numbers):
#     seen[numbers[i]] = [i]
#     prev = numbers[i]
#   else:
#     lst = seen[prev]

#     nxt = 0
#     if len(lst) == 2:
#       nxt = lst[-1] - lst[-2]
#     prev = nxt

#     if seen[nxt] is None:
#       seen[nxt] = (i,)
#     else:
#       if len(seen[nxt]) == 1:
#         seen[nxt] = (seen[nxt][0], i)
#       else:
#         seen[nxt] = (seen[nxt][1], i)
# print('part2:', prev)
