"""Write a program that takes an integer as input and returns an integer with reversed digit 
ordering."""
def reverse_digits(n):
    reversed_digits = int(str(n)[::-1])
    return reversed_digits
