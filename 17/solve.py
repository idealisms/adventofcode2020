import collections

inp = open('input').read()
lines = inp.strip().splitlines()

expand = 6
size = len(lines) + expand * 2
# board = [[['.'] * size for i in range(size)] for j in range(size)]
# for x in range(len(lines)):
#   for y in range(len(lines)):
#     board[expand][x+expand][y+expand] = lines[x][y]

# def count_active(board, x, y, z):
#   active = 0
#   for i in (-1, 0, 1):
#     for j in (-1, 0, 1):
#       for k in (-1, 0, 1):
#         if i == j == k == 0:
#           continue
#         if 0 <= x + i < size and 0 <= y + j < size and 0 <= z + k < size:
#           if board[x+i][y+j][z+k] == '#':
#             active += 1
#   return active

# def step(board):
#   new_board = [[['.'] * size for i in range(size)] for j in range(size)]
#   for x in range(size):
#     for y in range(size):
#       for z in range(size):
#         active = count_active(board, x, y, z)
#         if board[x][y][z] == '#' and active in (2, 3):
#           new_board[x][y][z] = '#'
#         elif board[x][y][z] == '.' and active == 3:
#           new_board[x][y][z] = '#'
#   return new_board

# for i in range(6):
#   board = step(board)

# total = 0
# for x in range(size):
#   for y in range(size):
#     for z in range(size):
#       if board[x][y][z] == '#':
#         total += 1
# print(total)

board = [[[['.'] * size for i in range(size)] for j in range(size)] for k in range(size)]
for x in range(len(lines)):
  for y in range(len(lines)):
    board[expand][expand][x+expand][y+expand] = lines[x][y]

def count_active(board, w, x, y, z):
  active = 0
  for h in (-1, 0, 1):
    for i in (-1, 0, 1):
      for j in (-1, 0, 1):
        for k in (-1, 0, 1):
          if h == i == j == k == 0:
            continue
          if 0 <= w + h < size and 0 <= x + i < size and 0 <= y + j < size and 0 <= z + k < size:
            if board[w+h][x+i][y+j][z+k] == '#':
              active += 1
  return active

def step(board):
  new_board = [[[['.'] * size for i in range(size)] for j in range(size)] for k in range(size)]
  for w in range(size):
    for x in range(size):
      for y in range(size):
        for z in range(size):
          active = count_active(board, w, x, y, z)
          if board[w][x][y][z] == '#' and active in (2, 3):
            new_board[w][x][y][z] = '#'
          elif board[w][x][y][z] == '.' and active == 3:
            new_board[w][x][y][z] = '#'
  return new_board

for i in range(6):
  print(i)
  board = step(board)

total = 0
for w in range(size):
  for x in range(size):
    for y in range(size):
      for z in range(size):
        if board[w][x][y][z] == '#':
          total += 1
print(total)

# time python solve.py
# real    0m21.956s
# user    0m21.860s
# sys     0m0.020s

# time pypy3 solve.py
# real    0m1.885s
# user    0m1.834s
# sys     0m0.051s
