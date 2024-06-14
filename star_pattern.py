def star_pattern_2(n):
    # Calculate the number of rows to print as it is 1 more than the input value
    n
    cal=n+1
    # Loop through each row
    for i in range(0, n):
        # Loop through each column in the current row
        for j in range(0, n):
            # Check if the current column is greater than or equal to the difference between cal and the current row number
            # If true, print a star, otherwise print a space
            if j >= cal - i:
                print("*", end="")
            else:
                print(" ", end="")
        # Move to the next row after printing all columns in the current row
        print("\n")
                            
# Set the number of rows to print
r=int(input("Enter the number if rows :"))
# Call the function to print the star pattern
# star_pattern_2(r)

def star_pattern_3(r):
    for i in range(0,r):
        for j in range(0,r):
            if (j>=i):
                print("*",end="")
            else:
                print(" ",end="")
        print("\n")
# star_pattern_3(r)
def star_pattern_4(r):
    C=(2*r-1)+1 
    f1=r+1
    f2=r-1
    for i in range(0,r+1):
        for j in range(0,C):
            if (j>=f1-i and j<=f2+i):
                print("*",end="")
            else:
                print(" ",end="")
        print("\n")
# star_pattern_4(r)
def star_pattern_5(r):
    C=(2*r-1)+1 
    f1=r+1
    f2=r-1
    k=True
    for i in range(0,r+1):
        for j in range(0,C):
            if (j>=f1-i and j<=f2+i and k==True):
                print("*",end="")
                k=False
            else:
                print(" ",end="")
                k=True
        print("\n")
# star_pattern_5(r)

def star_pattern_6(r):
    C=(2*r-1)+1 
    f1=r+1
    f2=r-1
    for i in range(1,r+1):
        for j in range(1,C):
            if (j<=f1-i or j>=f2+i):
                print("*",end="")
            else:
                print(" ",end="")
        print("\n")
# star_pattern_6(r)

def star_pattern_7(r):
    C=(2*r-1)+1 
    f1=r+1
    f2=r-1
    print(r)
    for i in range(0,r+1):
        k=1
        for j in range(0,C):
            if (j>=f1-i and j<=f2+i):
                print(k,end="")
                if j<r:
                    k+=1
                    # print(k)
                else:
                    k=k-1
            else:
                print(" ",end="")
        print("\n")
# star_pattern_7(r)

def star_pattern_8(r):
    C=(2*r-1)+1 
    f1=r+1
    f2=r-1
    print(r)
    for i in range(0,r+1):
        k=65
        for j in range(0,C):
            if (j<=f1-i or j>=f2+i):
                print(chr(k),end="")
                if j<r:
                    k+=1
                    # print(k)
                else:
                    k=k-1
            else:
                print(" ",end="")
        print("\n")
# star_pattern_8(r)

def star_pattern_9(r):
    n=(r+1)/2
    k=0
    for i in range(1,r+1):
        if i<=n:
            k+=1
        else:
            k-=1
        for j in range(1,r+1):
            if j>=5-k and j<=3+k:
                print("*",end="")
            else:
                print(" ",end="")
        print("\n")
# star_pattern_9(r)

def star_pattern_10(r):
    n=(r+1)/2
    k=0
    for i in range(1,r+1):
        if i<=n:
            k+=1
        else:
            k-=1
        for j in range(1,r+1):
            if j>=(n+1)-k and j<=(n-1)+k:
                print("*",end="")
            else:
                print("-",end="")
        print("\n")
# star_pattern_10(r)

# Enter your code here. Read input from STDIN. Print output to STDOUT
M, N = input().split()
M, N = int(M), int(N)

rcenter = int(M/2)+1
ccenter = int(N/2)+1
offset = rcenter - 1
for r in range(1, M+1):
    if r == rcenter:
        print('WELCOME'.center(N, '-'), end='')
    else:
        if rcenter > r:
            print(''.join(['.|.']*(r*2-1)).center(N, '-'), end='')
        else:
            print(''.join(['.|.']*(offset*2-1)).center(N, '-'), end='')
            offset = offset-1
    print()
    # ****






