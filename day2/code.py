
# reads file to string[]
def read_data(path):
  with open(path, 'r') as f:
    return [l.strip() for l in f.readlines()]

def parse(line):
  rules, word = line.split(':')
  word = word.strip()
  min_max, letter = rules.split(' ')
  low, high = min_max.split('-')

  return letter, low, high, word

def part_one(data):
  valids = []

  for line in data:
    letter, low, high, word = parse(line)
    count = sum(l == letter for l in word)
    valid = count <= int(high) and count >= int(low)
    valids.append(valid)

  print(sum(valids))

def part_two(data):
  valids = []

  for line in data[:]:
    letter, low, high, word = parse(line)
    l1, l2 = word[int(low)-1], word[int(high)-1]
    valid = (l1 != letter and l2 == letter) or (l1 == letter and l2 != letter)
    valids.append(valid)

  print(sum(valids))


data = read_data('data.txt')

part_one(data)
part_two(data)