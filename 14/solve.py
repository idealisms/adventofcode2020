inp = open('input').read()
lines = inp.strip().splitlines()

def apply(mask, n_str):
  out = ''
  for m, n in zip(mask, n_str):
    if m == 'X':
      out += n
    else:
      out += m
  return out

mem = {}
for line in lines:
  if line.startswith('mask'):
    mask = line.split(' = ')[1]
  else:
    addr, n = line.split('] = ')
    addr = addr[4:]
    n_str = '{0:036b}'.format(int(n))
    mem[addr] = apply(mask, n_str)

print(sum([int(n, 2) for n in mem.values()]))

def apply2(mask, n_str):
  out = ''
  for m, n in zip(mask, n_str):
    if m == '0':
      out += n
    else:
      out += m
  return out

def set_value(mem, addr, n):
  if addr.count('X') == 0:
    mem[addr] = n
    return
  set_value(mem, addr.replace('X', '0', 1), n)
  set_value(mem, addr.replace('X', '1', 1), n)

mem = {}
for line in lines:
  if line.startswith('mask'):
    mask = line.split(' = ')[1]
  else:
    addr, n = line.split('] = ')
    n = int(n)
    addr = '{0:036b}'.format(int(addr[4:]))
    addr = apply2(mask, addr)
    set_value(mem, addr, n)

print(sum(mem.values()))
