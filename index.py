def twoNumberSum(array,targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1,len(array) - 1):
            secondNum = array[j]

            if secondNum + firstNum == targetSum:
                return [firstNum,secondNum]

array = [3,5,-4,8,11,1,-1,6]
result = twoNumberSum(array,10)
print(result)