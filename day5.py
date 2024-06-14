"""
Drow a trangle shape using  print number  given a example
1
12
123
12345
123456

"""
def trangle(r):
    for i in range(r+1):
        for j in range(r+1):
            if (j>=i):
                print("")
            else:
                print(i ,end="")
        # print("\n")
# r=int(input("Enter the Row number : "))
# trangle(r)


"""
Print the  Pyramid Star Pattern

                *
              * * *
            * * * * *
          * * * * * * *
        
using run time values
"""

def Pyramid_star(r):
    for i in range(0,r+1):
        for j in range(0,r+1):
            pass
    

"""Count a every charceter in  given string """
def cunt(s):
    d={}
    for i in  s:
        # keys=keys()
        if i in d :
            d[i]+=1
            
        else:
            d[i]=1
    return d
print(cunt('banna'))


"""" Next question"""
def shrot_aseding(ls):
    l=[]
    for i in ls:
        c=float(i)
        l.append(c)
    return sorted(l)
print(shrot_aseding(['0.111','3.14','2.718','0.1','100.0','4.00004']))   

""""""         
    

