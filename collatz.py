# The collatz sequence, also called the 3n + 1 problem, is the simplest impossible math problem.
# From a starting number, n, follow three rules to get the next number in the sequence:
    # 1) if n is even, the next number is n / 2.
    # 2) if n is odd, the next number n is n * 3 + 1
    # 3) if n is 1, stop. Otherwise, repeat.
    
    # It is generally thought, buy so far not mathematically proven, that every starting number eventually terminates at 1.
    
import sys, time
    
print("""Collatz Sequence, or, the 3n + 1 Problem
      Modified by Agbolade Elijah
      
      The collatz sequence is a sequence of numbers produced fromm a starting number
      n, followint three rules:
      1) if n is even, the next number n is n / 2.
      2) if n is odd, the next number n is n * 3 + 1.
      3) if n is 1, stop. Otherwise, repeat.
      
      It is generally thougt, but so far not mathematically proven, that every starting number eventually terminates at 1.""")

print("Enter starting number (greater than 0) or QUIT: ")
response = input("> ")

if not response.isdecimal() or response == 0:
    print("You must enter an integer greater than 0.")
    sys.exit()
    
n = int(response)
print(n, end='', flush=True)

while n != 1:
    if n % 2 == 0: # if n is even
        n = n // 2
    else: # Otherwise, n is odd
        n = 3 * n + 1
        
    print(f", {n}", end='', flush=True)
    time.sleep(0.2)


    