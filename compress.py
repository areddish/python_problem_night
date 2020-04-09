# Compress
# https://www.hackerrank.com/challenges/compress-the-string/problem

#############################################
# Solution #1, not using groupby
#

# Take the input string and remove any space
in_str = input().strip()

# Start with the first character
cur = in_str[0]
count = 1

# We will now compare the current and previous characters to see if they
# are the same, if so we increment a counter. If not we will print out the
# current character and count.
for ch in in_str[1:]:
	# If the characters aren't equal we have a difference and this run
	# is complete, print it out.
	if ch != cur:
		print(f"({count}, {cur}) ", end="")
		cur = ch
		count = 1
	else:
		# Same character, just keep incrementing
		count += 1
# Make sure we print out the last character
print(f"({count}, {cur}) ")





#############################################
# Solution #2, using groupby
#

from itertools import groupby

# Take the input string and remove any space
in_str = input().strip()

# groupby will create an iterator of tuples with (character, group iter)
solution = []
for ch, group in groupby(in_str):
	# group is an iterator of the items in the group, we just care about
	# 			 the length for this problem.
	print(f"({len(list(group))}, {ch}) ",end="")
print()
