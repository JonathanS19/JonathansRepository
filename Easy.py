1)941. Valid Mountain Array
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        size = len(arr)
        flag = 0
        last = arr[-1]
        
        if size<3:
            return False
        
        for i in range(size):
            if arr[i] == arr[i+1] and arr[i]!=last:
                return False
            
            if flag == 0 :
                if arr[i]<arr[i+1]:
                    continue
                else:
                    flag = 1
                    
            elif flag == 1:
                if arr[i] == last :
                    return true
                if arr[i]>arr[i+1]:
                    continue
                else :
                    return False
            else:
                return False
        
        return True
2)860. Lemonade Change
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twenties = 0
        sum = 0

        for val in bills:
            sum+=val
        chg = sum - (len(bills)*5)
        print(chg)

        if chg in bills:
            return True

        for i,val1 in enumerate(bills):
            ovr = val1
            if val1 == 5:
                continue
            else:
                for val2 in bills[:i+1]:
                    ovr += val2
                    if ovr == chg:
                        return True
        return False

3)2206. Divide Array Into Equal Pairs
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        dist = list(set(nums))
        new = []

        for i,val1 in enumerate(dist):
            count = 0
            for j,val2 in enumerate(nums):
                if val1 == val2:
                    count += 1
                elif j == len(nums)-1:
                    if count%2 == 0:
                        continue
                    else:
                        return False
                else:
                    continue
        return True


