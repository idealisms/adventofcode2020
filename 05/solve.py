inp = open('input').read()
lines = inp.strip().splitlines()

hi = 0
seats = []
for line in lines:
  sid =  int(line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)
  hi = max(hi, sid)
  seats.append(sid)
print(hi)
seats.sort()
#print(seats)
for i, s in enumerate(seats):
  if seats[i+1] != s+1:
    print(seats[i] + 1)
    break
