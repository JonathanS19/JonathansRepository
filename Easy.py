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
            if val == 5:
                fives+=1
            elif val == 10:
                tens+=1
            else:
                twenties+=1

        chg = sum - (len(bills)*5)
        print(chg,"\n")
        ovr = 0

        for i,curr in enumerate(bills):
            ovr = curr
            if curr == chg:
                return True
            for j,next in enumerate(bills[i+1:]):
                ovr += next
                print(ovr)
                if next == chg:
                    return True
                elif ovr == chg:
                    return True
        return False
