def twoNumberSum(array,targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[right] + array[left]
        if currentSum == targetSum:
            return [array[left],array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right-=1
    return []

array = [3,5,-4,8,11,1,-1,6]
result = twoNumberSum(array,10)
print(result)