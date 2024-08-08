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
