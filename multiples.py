"""
    Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find and print the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_of_multiples(limit):
    total_sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum


limit = 1000

print(f"The sum of all multiples of 3 or 5 below {limit} is {sum_of_multiples(limit)}")
