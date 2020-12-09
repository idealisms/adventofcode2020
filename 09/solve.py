inp = open('input').read()
lines = list(map(int, inp.strip().splitlines()))

def test(values):
  targets = set()
  for i in range(25):
    for j in range(i+1, 25):
      targets.add(values[i] + values[j])
  if values[25] not in targets:
    return values[25]

part1 = 0
for start in range(len(lines) - 26):
  part1 = test(lines[start:start+26])
  if part1:
    print(part1)
    break

def part2():
  for start in range(len(lines)):
    total = lines[start]
    offset = 1
    while total < part1:
      total += lines[start+offset]
      if total == part1:
        print(min(lines[start:start+offset+1]) + max(lines[start:start+offset+1]))
        return
      offset += 1

part2()
