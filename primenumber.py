def is_prime(int):
  x = 2
  while int > x:
    solution = int % x
    if solution == 0:
      return True
    elif solution != 0:
      x += 1

number = 15485863
is_prime(number)
if is_prime(number) ==  True:
  print(f"{number} is a composite number")
else:
  print(f"{number} is a prime number")
