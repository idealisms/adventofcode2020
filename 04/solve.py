inp = open('input').read()
passports = inp.strip().split('\n\n')

valid = 0
for passport in passports:
  tokens = passport.split()
  found = set()
  for token in tokens:
    field = token.split(':')[0]
    if field != 'cid':
      found.add(field)
  if len(found) == 7:
    valid += 1

print(valid)

import re
valid = 0
for passport in passports:
  tokens = passport.split()
  found = {}
  for token in tokens:
    field, value = token.split(':')
    if field != 'cid':
      found[field] = value
  if (len(found) == 7
      and 1920 <= int(found['byr']) <= 2002
      and 2010 <= int(found['iyr']) <= 2020
      and 2020 <= int(found['eyr']) <= 2030
      and ((found['hgt'][-2:] == 'cm' and 150 <= int(found['hgt'][:-2]) <= 193)
        or (found['hgt'][-2:] == 'in' and 59 <= int(found['hgt'][:-2]) <= 76))
      and re.match(r'^[#][0-9a-f]{6}$', found['hcl'])
      and found['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
      and re.match(r'^\d{9}$', found['pid'])):
    valid += 1
print(valid)
