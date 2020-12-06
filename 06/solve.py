inp = open('input').read()
groups = inp.strip().split('\n\n')

total = 0
total2 = 0
for group in groups:
  line = group.replace('\n', '')
  total += len(set(line))
  letters = set(line)
  size = group.count('\n') + 1
  for l in letters:
    if line.count(l) == size:
      total2 += 1

print(total)
print(total2)