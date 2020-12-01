inp = open('input').read()
nums = [x for x in inp.split('\n') if x != '']
nums = list(map(int, nums))

size = len(nums)
def part1():
  for i in range(size):
    for j in range(i, size):
      n1 = nums[i]
      n2 = nums[j]
      if n1 + n2 == 2020:
        print(n1 * n2)
        return

def part2():
  for i in range(size):
    for j in range(i, size):
      for k in range(j, size):
        n1 = nums[i]
        n2 = nums[j]
        n3 = nums[k]
        if nums[i] + nums[j] + nums[k] == 2020:
          print(nums[i] * nums[j] * nums[k])
          return

part1()
part2()


