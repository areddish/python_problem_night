# doormat.py
# https://www.hackerrank.com/challenges/designer-door-mat/problem
N, M = [int(x) for x in input().split(" ")]

if N <= 5 or N >= 101 or M != 3 * N:
    print ("Invalid input. N must be > 5 and < 101, M must be N * 3")
    exit(-1)
    
# The welcome message
welcome = "Welcome"
# Symbol design
symbol = ".|."
# Starting count of dashes, this is the max number of dashes we need
# to render on a single side before the symbol. Each iteration we'll
# reduce this by the size of the symbol.
dash_start_count = (M - len(symbol)) // 2

# First, draw the top half
for i in range(N//2):
    print(dash_start_count*"-",end="")
    print(symbol*(i*2+1), end="")
    print(dash_start_count*"-")
    dash_start_count -= len(symbol)

# Now render out the welcome message
dashes = ((M - len(welcome)) // 2) * '-'
print(dashes+welcome+dashes)

# Lastly render the bottom.
dash_start_count += len(symbol)
for i in range(N//2-1,-1,-1):
    print(dash_start_count*"-",end="")
    print(symbol*(i*2+1), end="")
    print(dash_start_count*"-")
    dash_start_count += len(symbol)