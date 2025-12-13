'''Write a function fizzbuzz_variant(n) that returns a list of strings for numbers 1..n where:

multiples of 3 → "Fizz"
multiples of 5 → "Buzz"
multiples of both 3 and 5 → "FizzBuzz"
primes → "Prime" (if a number is prime, print "Prime" instead of other tags)
otherwise the number as string
'''

import math

def is_prime(number):
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0:
        return False
    
    square_root = int(math.sqrt(number))
    for divider in range(3, square_root + 1, 2):
        if number % divider == 0:
            return False 
    
    return True  

def fizz_buzz(max_number):
    result = []
    for number in range(1, max_number + 1):
        if is_prime(number):
            result.append("Prime")
            continue

        if number % 3 == 0 and number % 5 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))
    return result

if __name__ == "__main__":
    game_results = fizz_buzz(55)
    print(game_results)
        
    
    
