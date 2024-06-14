"""Task 1
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird"""


import math
import os
import random
import re
import sys
class Solution:
    def __init__(self,n):
        self.n = n
    def Conditions(self):
        if self.n%2==0  and (self.n>2 and self.n<5):
            print("Not Weird")
        elif self.n%2==0 and (self.n>6 and self.n<=20):
            print("Weird")
        elif (self.n%2==0 and self.n>20):
            print("Not Weird")
        else:
            print("Weird")
            
if __name__ == '__main__':
    
    n = int(input().strip())
    obj=Solution(n)
    obj.Conditions()
