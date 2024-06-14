"""You are given a string  consisting only of digits 0-9, commas ,, and dots .

Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in .

It’s guaranteed that every comma and every dot in  is preceeded and followed by a digit.

Sample Input 0

100,000,000.000
Sample Output 0

100
000
000
000"""


regex_pattern = r"\W"	# Do not delete 'r'.


import re
print("\n".join(re.split(regex_pattern,"100,000,000.000")))



#===========================================================================================================================================
#NOTE - Q2

"""Task

You are given a string .
Your task is to find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.

Input Format

A single line of input containing the string .

Constraints


Output Format

Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

Sample Input

..12345678910111213141516171820212223
Sample Output

1
Explanation

.. is the first repeating character, but it is not alphanumeric.
1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111."""




import re

def find_repeating_character(s):
    # Define a regex pattern to find consecutive repetitions of alphanumeric characters
    pattern =r'([a-zA-Z0-9])\1'

    # Search for the pattern in the input string
    match = re.search(pattern, s)

    if match:
        # If a match is found, print the first occurrence of the repeating character
        print(match.group(1))
    else:
        # If no repeating character is found, print -1
        print(-1)

# Input
input_string = input("")

# Call the function with the input string
find_repeating_character(input_string)
