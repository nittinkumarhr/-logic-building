"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
l1=["2","4","3"]
l2=["5","6","4"]
l1=l1[::-1]
l2=l2[::-1]
s=""
s2=""
for i in l1:
    s+=i
for j in l2:
    s2 +=j
print(int(s)+int(s2))