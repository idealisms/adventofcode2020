import collections

inp = open('input').read()
lines = inp.strip().splitlines()

def solve1(tokens):
  # print('solve', tokens)
  if '(' not in tokens:
    n = tokens[0]
    for i in range(1, len(tokens), 2):
      if tokens[i] == '*':
        n *= tokens[i+1]
      else:
        n += tokens[i+1]
    return n
  else:
    popen = -1
    for i, token in enumerate(tokens):
      if token == '(':
        popen = i
      elif token == ')':
        return solve1(tokens[:popen] + [solve1(tokens[popen+1:i])] + tokens[i+1:])

def make_tokens(line):
  tokens = []
  for c in line:
    if c == ' ':
      continue
    if c in '123456789':
      tokens.append(int(c))
    else:
      tokens.append(c)
  return tokens

total = 0
for line in lines:
  n = solve1(make_tokens(line))
  # print(n)
  total += n
print('part1:', total)

def solve2(tokens):
  # print('solve', tokens)
  if '(' not in tokens:
    if '+' in tokens and '*' in tokens:
      i = tokens.index('+')
      if i == 1:
        return solve2([solve2(tokens[i-1:i+2])] + tokens[i+2:])
      else:
        return solve2(tokens[:i-1] + [solve2(tokens[i-1:i+2])] + tokens[i+2:])
    else:
      n = tokens[0]
      for i in range(1, len(tokens), 2):
        if tokens[i] == '*':
          n *= tokens[i+1]
        else:
          n += tokens[i+1]
      return n
  else:
    popen = -1
    for i, token in enumerate(tokens):
      if token == '(':
        popen = i
      elif token == ')':
        return solve2(tokens[:popen] + [solve2(tokens[popen+1:i])] + tokens[i+1:])

total = 0
for line in lines:
  n = solve2(make_tokens(line))
  # print(n)
  total += n
print('part2:', total)