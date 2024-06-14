"""#NOTE -Q.1 
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example





: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
def list_method() :
    N = int(input())
    l=[]
    for i in range(0,N):
        name_method,*items=input().split(' ')
        # l=len(items)
        # print(items[0],type(items))
        # l.insert(items[0],items[1])
        
        
        if name_method =='append':
            for item in items:
                l.append(int(item))
        if name_method =='insert':
            # for j in range(l+1):
                l.insert(int(items[1]),int(items[0]))
        if name_method == 'remove':
            l.remove(int(items[0]))
        if name_method =='sort':
            l.sort()
        if name_method =='pop':
            l.pop()
        if name_method =='print':
            print(int(l))
        if name_method =='reverse':
            print(l.reverse())
            
if __name__ == '__main__':
    n = int(input())
    l=[]
    for i in range(n):
        items=input().split()
        l.append(tuple(items))
    t=tuple(l)
    print(t)
    print(type(t))
    print(hash(t))
        
                
                
