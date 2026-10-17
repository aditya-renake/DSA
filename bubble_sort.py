nums=[5,1,4,2,8,7,3,6]

n=len(nums)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)

#time complexity of bubble sort is O(n^2) and space complexity is O(1)