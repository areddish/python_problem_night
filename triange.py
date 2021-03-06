# triangle.py
# https://www.hackerrank.com/challenges/python-quest-1/problem


#####
# Solution 1

# Example on how to do it with strings, but not accepted by hackerrank due to string operation.

for i in range(1,int(input())):
    for j in range(i):
        print(i, end="")
    print()

#####
# Solution 2

# Example on how to do it with strings, but not accepted by hackerrank due to string operation.

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (str(i)*i)


#####
# Solution 3

# Mathy solution. Takes advantage of the fact that dividing a power of 10 by 9 = 11.11111111 and then uses
# integer division to truncate. So 100//9 = 11, 1000//9 = 111, and so on.

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (i*(10**i)//9)
