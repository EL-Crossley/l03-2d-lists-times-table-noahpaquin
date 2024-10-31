def timestable(nums):
    table = [[1,2,3,4,5],[2,4,6,8,10],[3,6,9,12,15],[5,10,15,20,25]]
    num = nums
    return table[0:num]


nums = int(input())
print(timestable(nums))
