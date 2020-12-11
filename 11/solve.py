inp = open('input').read()
seats = inp.strip().splitlines()

def cnt_adj(seats, r, c, v):
  cnt = 0
  for r_ in range(r-1, r+2):
    for c_ in range(c-1, c+2):
      if r_ == r and c_ == c:
        continue
      if r_ >= 0 and c_ >= 0 and r_ < len(seats) and c_ <len(seats[r]):
        if seats[r_][c_] == v:
          cnt += 1
  return cnt

def new_val(seats, r, c):
  if seats[r][c] == 'L':
    if cnt_adj(seats, r, c, '#') == 0:
      return '#'
  if seats[r][c] == '#' and cnt_adj(seats, r, c, '#') >= 4:
    return 'L'
  return seats[r][c]

def part1(seats):
  while True:
    new_seats = []
    for r, row in enumerate(seats):
      new_row = ''
      for c, val in enumerate(row):
        new_row += new_val(seats, r, c)
      new_seats.append(new_row)
    #print(seats)
    #print(new_seats)
    #print('-' * 40)

    if new_seats == seats:
      occ = 0
      for row in new_seats:
        for c in row:
          if c == '#':
            occ += 1
      print(occ)
      return
    seats = new_seats


part1(seats)

def can_see(seats, r, c, dr, dc):
  while True:
    r += dr
    c += dc
    if r < 0 or r == len(seats) or c < 0 or c == len(seats[0]):
      return False
    if seats[r][c] == 'L':
      return False
    if seats[r][c] == '#':
      return True

def cnt_see(seats, r, c):
  cnt = 0
  for dr in range(-1, 2):
    for dc in range(-1, 2):
      if dr == 0 and dc == 0:
        continue
      if can_see(seats, r, c, dr, dc):
        cnt += 1
  return cnt

def new_val2(seats, r, c):
  if seats[r][c] == 'L':
    if cnt_see(seats, r, c) == 0:
      return '#'
  if seats[r][c] == '#' and cnt_see(seats, r, c) >= 5:
    return 'L'
  return seats[r][c]

def part2(seats):
  while True:
    new_seats = []
    for r, row in enumerate(seats):
      new_row = ''
      for c, val in enumerate(row):
        new_row += new_val2(seats, r, c)
      new_seats.append(new_row)
    #print(seats)
    #print(new_seats)
    #print('-' * 40)
    #return

    if new_seats == seats:
      occ = 0
      for row in new_seats:
        for c in row:
          if c == '#':
            occ += 1
      print(occ)
      return
    seats = new_seats

part2(seats)