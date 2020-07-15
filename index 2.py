def twoNumberSum(array,targetSum):
    nums = {}
    for num in array:
        secondNum = targetSum - num
        if secondNum in nums:
            return [num,secondNum]
        else:
            nums[num] = True
    
    return []

array = [3,5,-4,8,11,1,-1,6]
result = twoNumberSum(array,10)
print(result)