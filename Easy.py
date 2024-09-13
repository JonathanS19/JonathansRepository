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

4)58. Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #No of whitespaces
        no_spcs  = s.count(" ")
        lst_spc = s.rindex(" ")
        count = 0

        for i in range(lst_spc,len(s)-1):
            if i != " " or "-":
                count+=1
        
        if count == 0:
            nxt_spc = s.find(" ",0,)
            if s[]

        print(no_spcs)
        return count

        (or)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            lst_spc = s.rindex(" ")
            
        count = 0

        for i in range(lst_spc,len(s)-1):
            if i != " " or "-":
                count+=1
        
        if count!=0:
            return count

        else:
            for i in range(1,len(s)-1):
                count1 = 0
                no_spcs  = s.count(" ")-i
                for j in range(len(s)-1):
                    if s[j] == " ":
                        count1+=1
                        # print("count : ",count1)
                        # print("no of spaces : ",no_spcs)
                        if count1 == no_spcs and s[j+1] != " " :
                            for k in range(j+1,len(s)-1):
                                if k != " ":
                                    count+=1
                                elif k == " ":
                                    break
                            count-=1
                            return count 
                    else:
                        continue
        return 0
5)1945. Sum of Digits of String After Convert
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alp = {}
        count = 1

        for i in range(97,123):
            alp[chr(i)] = str(count)
            count+=1

        num_val = 0

        if k == 1:
            for val in s :
                lst = list(alp[val])
                for val in lst:
                    num_val+=int(val)
        else :
            for val in s :
                cnt = 1
                lst1 = list(alp[val])
                # print("lst1 : ",lst1)
                for val in lst1:
                    num_val += int(val)
                # print("sum1 : ",num_val)

            while cnt!=k :
                lst2 = list(str(num_val))
                num_val = 0
                # print("lst2 : ", lst2)
                for val in lst2:
                    num_val+=int(val)
                # print("sum2 :",num_val)
                cnt+=1
        return num_val
6)2287. Rearrange Characters to Make Target String
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        chars = list(target)
        occ = {}
        for char in chars:
            count = 0
            for val in s:
                if char == val:
                    count+=1
            if char in occ:
                continue
            else:
                occ.update({char : count})
        if len(occ) == 1 and len(chars) == min(occ.values()):
            return 1
        return min(occ.values())
7)1684. Count the Number of Consistent Strings
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed = str(list(allowed))
        print(allowed)

        for word in words :
            flag = 0
            for l in word:
                print("l :",l)
                if l in allowed:
                    flag = 0
                else:
                    flag = 1
                    break
                print("flag : ",flag)
            if flag == 0:
                count+=1
            print("Count : ",count)

        return count
8)2220. Minimum Bit Flips to Convert Number
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = format(start,'b')
        goal = format(goal,'b')

        count = 0 
        
        for val1,val2 in zip(start[::-1],goal[::-1]):
            if val1 == val2:
                continue
            else:
                count+=1

        if len(start) != len(goal):
            max_val = max(len(start),len(goal))
            min_val = min(len(start),len(goal))

            count+=(abs(len(start)-len(goal)))
            for i in range(max_val - min_val) :
                if len(goal) == max_val:
                    if goal[i] == '0':
                        count-=1
                else:
                    if start[i] == '0':
                        count-=1


        return count
9)27. Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums :
            return len(nums)
        else:
            #count of target val
            count = 0 
            for num in nums :
                if num == val:
                    count+=1
            for i in range(0,count):
                for i in range(0,len(nums)-1):
                    if nums[i] == val:
                        del nums[i]
                    else:
                        continue
            print(nums)
            return len(nums)
10)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        
        if len(s)>len(t)
        for ltr1 in t:
            print("s",s)
            for i,ltr2 in enumerate(s):
                if ltr1 == ltr2:
                    s.pop(i)
                    break
        if s!=[]:
            return False
        return True
