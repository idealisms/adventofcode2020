import collections

inp = open('input').read()
tinp = '389125467'
nums = inp.strip()
nums = [int(n) for n in nums]

class Node(object):
  def __init__(self, n):
    self.n = n
    self.next = None

  def __repr__(self):
    return f'({self.n}, {self.next.n})'

def init(nums, size):
  index = [None] + [Node(n) for n in range(1, size + 1)]
  start = nums + list(range(len(nums) + 1, size + 1))
  for i, n in enumerate(start):
    if i == len(start) - 1:
      index[n].next = index[start[0]]
    else:
      index[n].next = index[start[i+1]]
  return index

def run(index, cur, steps):
  for _ in range(steps):
    if _ > 0 and _ % 1000000 == 0:
      print('step', _)
    # print(index)
    pickup_start = cur.next

    dest = cur.n - 1
    if dest == 0:
      dest = len(index) - 1
    while dest in (
        pickup_start.n,
        pickup_start.next.n,
        pickup_start.next.next.n):
      dest -= 1
      if dest == 0:
        dest = len(index) - 1

    cur.next = pickup_start.next.next.next
    dest_node = index[dest]
    dest_node.next, pickup_start.next.next.next = pickup_start, dest_node.next

    cur = cur.next

index = init(nums, len(nums))
run(index, index[nums[0]], 100)
node = index[1].next
answer = ''
while node.n != 1:
  answer += str(node.n)
  node = node.next
print('part1:', answer)  # 27865934

index = init(nums, 1000000)
run(index, index[nums[0]], 10000000)
print('part2:', index[1].next.n * index[1].next.next.n)
