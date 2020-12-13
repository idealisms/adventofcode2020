inp = open('input').read()
lines = inp.strip().splitlines()

target = int(lines[0])
buses = [int(n) for n in lines[1].split(',') if n != 'x']

def part1():
  for i in range(target, target + 700):
    for bus in buses:
      if i % bus == 0:
        print(bus * (i - target))
        return

part1()

positions = [int(n) if n != 'x' else 'x' for n in lines[1].split(',')]
times = []
for bus in buses:
  times.append((bus, positions.index(bus)))

# times = [(37, 0), (41, 27), (601, 37), (19, 49), (17, 54), (23, 60), (29, 66), (443, 68), (13, 81)]

t = 0
step = 37
for m, offset in times[1:]:
  while True:
    if (t + offset) % m == 0:
      # print(t)
      step = m * step
      break
    t += step
print(t)