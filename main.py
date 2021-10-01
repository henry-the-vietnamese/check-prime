#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         12/8/2021
# Description:  The file where we can time how long each function takes to execute.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#

"""
The time module has a function called time which is able to perform the timing.
The check-prime-functions module comprises 3 functions to measure.
"""

from time import time
import check_prime_functions as func


print('A program to check prime number.',
      'Return True if it is, False otherwise.',
      sep = '\n',
)

n = int(input("\nEnter a number for evaluation: "))

func.line()

# function_a
t0 = time()
print(f'{n} is {func.is_prime_a(n)}')
func.prime_lessthan(func.is_prime_a)
t1 = time()
print(f'Function A: time taken = {round(t1 - t0, 4)} seconds.')

func.line()

# function_b
t2 = time()
print(f'{n} is {func.is_prime_b(n)}')
func.prime_lessthan(func.is_prime_b)
t3 = time()
print(f'Function B: time taken = {round(t3 - t2, 4)} seconds.')

func.line()

# function_c
t4 = time()
print(f'{n} is {func.is_prime_c(n)}')
func.prime_lessthan(func.is_prime_c)
t5 = time()
print(f'Function C: time taken = {round(t5 - t4, 4)} seconds.')
