inp = open('input').read()
lines = list(map(int, inp.strip().splitlines()))

lines.sort()

jolt = 0
diff = {1: 0, 2: 0, 3: 0}
for j in lines:
  d = j - jolt
  diff[d] += 1
  jolt = j
print(diff[1] * (diff[3] + 1))

jolts = set(lines)
target = lines[-1]

mem = {}
def cnt(j):
  if j in mem:
    return mem[j]
  if j == target:
    return 1
  total = 0
  for i in (1, 2, 3):
    if j + i in jolts:
      total += cnt(j + i)
  mem[j] = total
  return total

print(cnt(0))