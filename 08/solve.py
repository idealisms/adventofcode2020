inp = open('input').read()
lines = inp.strip().splitlines()

acc = 0
seen = set()
inst = 0
commands = []
while True:
  if inst in seen:
    break
  seen.add(inst)
  line = lines[inst]
  #print(inst, line)
  cmd, amt = line.split(' ')
  if cmd in ('jmp', 'nop'):
    commands.append(inst)
  amt = int(amt)
  if cmd == 'acc':
    acc += amt
    inst += 1
  elif cmd == 'jmp':
    inst += amt
  elif cmd == 'nop':
    inst += 1
print('part1', acc)

def run(lines):
  acc = 0
  seen = set()
  inst = 0
  while True:
    if inst == len(lines):
      return acc
    if inst in seen:
      return
    seen.add(inst)
    line = lines[inst]
    cmd, amt = line.split(' ')
    amt = int(amt)
    if cmd == 'acc':
      acc += amt
      inst += 1
    elif cmd == 'jmp':
      inst += amt
    elif cmd == 'nop':
      inst += 1


for cmd_to_switch in commands:
  new_lines = lines[:]
  cmd, amt = new_lines[cmd_to_switch].split(' ')
  if cmd == 'nop':
    new_lines[cmd_to_switch] = 'jmp ' + amt
  else:
    new_lines[cmd_to_switch] = 'nop ' + amt
  #print('try', cmd_to_switch)
  res = run(new_lines)
  if res is not None:
    print('part2', res)
    break
