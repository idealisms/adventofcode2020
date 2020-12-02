inp = open('input').read()
lines = [x for x in inp.strip().split('\n') if x != '']

valid = 0
for line in lines:
  repeats, letter, password = line.split(' ')
  min_r, max_r = list(map(int, repeats.split('-')))
  letter = letter[0]
  cnt = password.count(letter)

  if min_r <= cnt <= max_r:
    valid += 1

print('part1:', valid)

valid = 0
for line in lines:
  repeats, letter, password = line.split(' ')
  min_r, max_r = list(map(int, repeats.split('-')))
  letter = letter[0]
  cnt = 0
  if password[min_r-1] == letter:
    cnt += 1
  if password[max_r-1] == letter:
    cnt += 1
  if cnt == 1:
    valid += 1
print('part2:', valid)