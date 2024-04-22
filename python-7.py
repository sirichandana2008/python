#Sorting
#Binary search
nums=[12,34,2,56,90,33,89,120,20]
#Time complexity of linear search is order of n where n is length of list
#Function to sort a list
nums=sorted(nums)
target=89
left=0
right=len(nums)-1
found=False
#Time complexity is O(log n) i.e order of log n
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        found=True
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
if found==True:
    print("Target found")
else:
    print("Target Not Found")
