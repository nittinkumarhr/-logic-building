"""Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False."""
def is_leap(year):
    leap = False
    if year%4==0:
        if year%100!=0:
            leap=True
    # Write your logic here
   
    return leap

year = int(input())
print(is_leap(year))
        