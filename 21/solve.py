import collections
import itertools

inp = open('input').read()
tinp = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''

lines = inp.strip().splitlines()

m = collections.defaultdict(list)
all_ingredients = set()
ingredient_lines = []
for line in lines:
  ingredients, cont = line.split(' (contains ')

  ingredients = set(ingredients.split(' '))
  ingredient_lines.append(ingredients)
  all_ingredients.update(ingredients)

  allergens = cont[:-1].split(', ')
  for allergen in allergens:
    m[allergen].append(ingredients)

might_contain = {}
for allergen, sets in m.items():
  inter = sets[0]
  for s in sets[1:]:
    inter = inter.intersection(s)
  might_contain[allergen] = inter

safe_ingredients = all_ingredients
for ingredients in might_contain.values():
  safe_ingredients = safe_ingredients.difference(ingredients)
# print(safe_ingredients)
total = 0
for ingredients in ingredient_lines:
  for safe_ingredient in safe_ingredients:
    if safe_ingredient in ingredients:
      total += 1
print('part1:', total)

for allergen, sets in m.items():
  filtered = []
  for s in sets:
    filtered.append(s - safe_ingredients)
  final = filtered[0]
  for s in filtered[1:]:
    final = final.intersection(s)
  m[allergen] = final

known_map = {}
while True:
  solved = {}
  for allergen, ingredients in m.items():
    if len(ingredients) == 1:
      ing = list(ingredients)[0]
      known_map[allergen] = ing
      solved[allergen] = ing
  if len(solved) == 0:
    break
  known_map.update(solved)
  for allergen, ingredient in solved.items():
    del m[allergen]
  to_remove = set(ing for ing in solved.values())
  for allergen, ingredients in m.items():
    m[allergen] = ingredients - to_remove

ingredients = []
for allergen in sorted(known_map.keys()):
  ingredients.append(known_map[allergen])
print('part2:', ','.join(ingredients))
