

for num in range(1,101): # iterates thorugh all numbers from 1 to 100
  #check that the number is divisible by both 3 and 5
  if(num%3==0 and num%5==0):
    print("FizzBuzz")
  #check that the number is divisible by 3
  elif(num%3 == 0):
    print("Fizz")
  #check that the number is divisible by 5
  elif(num%5 == 0):
    print("Buzz")
  #if it's not divisible by either 3 or 5 print the number
  else:
    print(num)

