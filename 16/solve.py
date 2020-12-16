import collections
import itertools

inp = open('input').read()
rules, your_ticket, nearby_tickets = inp.strip().split('\n\n')

# rules = '''class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50'''

# nearby_tickets = '''nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12'''

r_map = {}
for line in rules.splitlines():
  name, v = line.split(': ')
  r1, r2 = v.split(' or ')
  r_map[name] = (
    [int(n) for n in r1.split('-')],
    [int(n) for n in r2.split('-')])

def is_valid(num):
  for r1, r2 in r_map.values():
    if r1[0] <= num <= r1[1]:
      return True
    if r2[0] <= num <= r2[1]:
      return True
  return False

error_rate = 0
valid_tickets = []
for ticket in nearby_tickets.splitlines()[1:]:
  nums = [int(n) for n in ticket.split(',')]
  valid_ticket = True
  for num in nums:
    if not is_valid(num):
      error_rate += num
      valid_ticket = False
      break
  if valid_ticket:
    valid_tickets.append(nums)
print(error_rate)

def poss(rs, col):
  for nums in valid_tickets:
    n = nums[col]
    if n < rs[0][0] or (rs[0][1] < n < rs[1][0]) or rs[1][1] < n:
      return False
  return True

COLS = len(r_map)
possible_cols = collections.defaultdict(set)
for name, rules in r_map.items():
  for i in range(COLS):
    if poss(rules, i):
      possible_cols[name].add(i)

# There's only one possible ordering. In fact, there's one
# column that only works with one field, one column that works
# with 2 fields, one column that works with 3 fields, etc. So
# we can just assign them in order.
order = [None] * COLS
used = set()
for i in range(COLS):
  for name, set_ in possible_cols.items():
    if len(set_) == i + 1:
      s = set_.difference(used)
      if len(s) != 1:
        raise Exception(name)
      order[list(s)[0]] = name
      used.add(list(s)[0])
      break

# print(order)

ticket_nums = [int(n) for n in your_ticket.splitlines()[1].split(',')]
prod = 1
for i, name in enumerate(order):
  if name.startswith('departure'):
    prod *= ticket_nums[i]
print(prod)