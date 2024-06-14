"""You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True"""

if __name__ == '__main__':
    s = input()
    import re

def find_in_string(s):
    alphanumeric = re.search(r'\w', s) is not None  #-it is check  (a-z, A-Z and 0-9).
    alphabetical = re.search(r'[a-zA-Z]', s) is not None # - it is check (a-z,A-z)
    digits = re.search(r'\d', s) is not None
    lowercase = re.search(r'[a-z]', s) is not None
    uppercase = re.search(r'[A-Z]', s) is not None

    return alphanumeric, alphabetical, digits, lowercase, uppercase


alphanumeric, alphabetical, digits, lowercase, uppercase = find_in_string(s)

print(f"{alphanumeric}")
print(f"{alphabetical}")
print(f"{digits}")
print(f"{lowercase}")
print(f"{uppercase}")

#Replace all ______ with rjust, ljust or center. 


