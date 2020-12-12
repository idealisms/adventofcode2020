inp = open('input').read()
lines = inp.strip().splitlines()
#lines = list(map(int, lines))

# 0 N
# 1 E
# 2 S
# 3 W
facing = 1

x = y = 0

for line in lines:
  cmd = line[0]
  n = int(line[1:])
  if cmd == 'R':
    facing  = (facing + n/90) % 4
  elif cmd == 'L':
    facing  = (facing - n/90 + 4) % 4
  elif cmd == 'E':
    x += n
  elif cmd == 'N':
    y += n
  elif cmd == 'W':
    x -= n
  elif cmd == 'S':
    y -= n
  elif cmd == 'F':
    if facing == 0:
      y += n
    elif facing == 1:
      x += n
    elif facing == 2:
      y -= n
    elif facing == 3:
      x -= n

print(abs(x) + abs(y))

wx = 10
wy = 1
x = y = 0

for line in lines:
  cmd = line[0]
  n = int(line[1:])
  if cmd == 'E':
    wx += n
  elif cmd == 'N':
    wy += n
  elif cmd == 'W':
    wx -= n
  elif cmd == 'S':
    wy -= n
  elif cmd == 'R':
    # 4n 10e -> 10s 4e -> 10w 4s
    for i in range(int(n / 90)):
      wx, wy = (wy, -wx)
  elif cmd == 'L':
    for i in range(int(n / 90)):
      wx, wy = (-wy, wx)
  elif cmd == 'F':
    x += n * wx
    y += n * wy

print(abs(x) + abs(y))

