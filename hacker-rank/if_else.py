"""
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
"""

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 1 and n < 2:
        print("Weird")
    if n % 2 == 0 and 5 >= n >= 2:
        print("Not Weird")
    if n % 2 == 0 and 20 >= n >= 6:
        print("Weird")
    if n % 2 == 0 and n > 20:
        print("Not Weird")
    if n % 2 == 1:
        print("Weird")