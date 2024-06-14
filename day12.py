nums =[]
for i in range(0,5):
    nums.append(int(input("enter the number")))
trget=18
empty_list=[]
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if trget==nums[i]+nums[j]:
            empty_list.append(i+1)
            empty_list.append(j+1)
            print(empty_list)
            break