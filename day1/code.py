
# reads file to int[]
def read_data(path):
  with open(path, 'rb') as f:
    return [int(l.strip()) for l in f.readlines()]
    
'''
tries to add all numbers to find n, m which gives desired_sum
returns the product of n, m
'''
def find_product(numbers, desired_sum):
  for n in numbers:
    for m in numbers: 
      if n + m == desired_sum: 
        return n*m

data = read_data('data.txt')
product = find_product(data, 2020)

print(f'desired product is {product}')