inp = open('input').read()
lines = inp.strip().splitlines()
parents = {}  # For part 1
dag = {}  # For part 2
for line in lines:
  lhs, rhs = line.split(' contain ')
  lhs = lhs[:-len(' bags')]
  rhs = rhs[:-1]
  dag[lhs] = {}
  if rhs != 'no other bags':
    rhs = rhs.split(', ')
    for bag in rhs:
      name = bag[2:bag.rfind(' ')]
      parents.setdefault(name, set()).add(lhs)
      dag[lhs][name] = int(bag[0])  # Only single digit values

def contains(bag, acc):
  if bag not in parents:
    return acc
  acc.update(parents[bag])
  for b in parents[bag]:
    acc.update(contains(b, acc))
  return acc

target = 'shiny gold'
part1 = set()
contains(target, part1)
print(len(part1))

def count(bag):
  if bag not in dag or len(dag[bag]) == 0:
    return 1
  total = 1  # Include the bag itself.
  for b, cnt in dag[bag].items():
    total += cnt * count(b)
  return total

print(count(target) - 1)  # Subtract the shiny gold bag itself.
