# CHALLENGE 1

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

print(sum_to(6))
print(sum_to(10))


# CHALLENGE 2

def largest(numbers):
  largest = 0
  for num in numbers:
    if num > largest:
      largest = num
  return largest

print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))



# CHALLENGE 3

def occurrences(string, substr):
  stripped_string = string.replace(substr, '')
  return (len(string) - len(stripped_string)) // len(substr)

print(occurrences('fleep floop', 'e'))
print(occurrences('fleep floop', 'p'))
print(occurrences('fleep floop', 'ee'))
print(occurrences('fleep floop', 'fe'))



# CHALLENGE 4

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))