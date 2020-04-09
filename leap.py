# Leap year
# https://www.hackerrank.com/challenges/write-a-function/problem


# The year can be evenly divided by 4, is a leap year, unless: 
# The year can be evenly divided by 100, it is NOT a leap year, unless: 
# The year is also evenly divisible by 400. Then it is a leap year.

#######################
# Solution 1

# if's
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 != 0:
                leap = False
            else:
                leap = True
        else:
            leap = True
    
    return leap


#######################
# Solution 2

# One-liner boolean
def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

