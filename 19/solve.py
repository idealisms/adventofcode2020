import itertools

inp = open('input').read()
rule_lines, messages = inp.strip().split('\n\n')

rules = {}
for line in rule_lines.splitlines():
  n, rule = line.split(': ')
  rules[n] = rule

mem = {}
def expand(rule):
  if rule in ('"a"', '"b"'):
    return set(rule[1])

  if ' ' not in rule:
    return expand(rules[rule])

  if rule in mem:
    return mem[rule]

  # print('expand', rule)

  if '|' not in rule:
    tokens = rule.split(' ')
    possible = expand(rules[tokens[0]])
    for r in tokens[1:]:
      additional = expand(rules[r])
      possible = set(a + b for a, b in itertools.product(possible, additional))
    mem[rule] = possible
    return possible
  else:
    i = rule.find('|')
    lhs = expand(rule[:i-1])
    rhs = expand(rule[i+2:])
    possible = lhs.union(rhs)
    mem[rule] = possible
    return possible

answers_zero = expand("0")
# print(len(answers_zero))

messages = messages.splitlines()
# print(len(messages))
total = 0
max_len = 0
for message in messages:
  max_len = max(max_len, len(message)) # 80
  if message in answers_zero:
    # print(message)
    total += 1
print('part1:', total)

# 0: 8 11
# 8: 42 | 42 8   # Repetitions of 42
# 11: 42 31 | 42 11 31 # 42 31, 42 42 31 31
a42 = expand("42")
a42_len = len(list(a42)[0])
a31 = expand("31")
a31_len = len(list(a31)[0])
# print(max_len, a42_len, a31_len) # 80, 8 8

def count_trailing(message, values):
  cnt = 0
  while True:
    match = False
    for value in values:
      if message.endswith(value):
        match = True
        break
    if not match:
      return cnt
    else:
      cnt += 1
      message = message[:-8]

total = 0
for message in messages:
  cnt_31s = count_trailing(message, a31)
  if cnt_31s == 0:
    continue
  message = message[:-8 * cnt_31s]
  # print(cnt_31s, message)
  cnt_42s = count_trailing(message, a42)
  if cnt_42s * 8 == len(message) and cnt_42s > cnt_31s:
    total += 1

print('part2:', total)
