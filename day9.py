"""Task -1.
Read a given string, change the character at a given index and then print the modified string.
Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert
Returns

string: the altered string
Input Format

The first line contains a string, .
The next line contains an integer , the index location and a string , separated by a space.

Sample Input

STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
Sample Output

abrackdabra"""


def mutate_string(string, position, character):
    string = input()
    position,character =input().split()
    l=list(string)
    l[int(position)]=character
    s=''.join(l)
    return s


"""Task-2
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
Concep"""

def count_substring():
    # ls=len(string)
    string=input()
    sub_string=input()
    k=0
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            k+=1
    return k
