1)1894. Find the Student that Will Replace the Chalk
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        while True :
            for i,val in enumerate(chalk):
                if k < val:
                    return i
                else:
                    k-=val
2)7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        lst = list(str(x))
        lst = lst[::-1]
        new = []

        if '-' in lst:
            new.append('-')
            for i,val in enumerate(lst):
                if lst[0] == '0' or val == '-':
                    continue
                else:
                    new.append(val)
        
        else:
            for i,val in enumerate(lst):
                if i == 0 and val == '0':
                    continue
                else:
                    new.append(val)

        res = ""
        for val in new:
            res+=val
        if res != "":
            res = int(res)
        else:
            return 0

        if res < -2**31 or res > 2**31 - 1 or res == 0:
            return 0
        else:
            return res
3)2586. Count the Number of Vowel Strings in Range
class Solution:
    def originalDigits(self, s: str) -> str:
        alp = {}
        lst =list(s)

        for ltr1 in s:
            count = 0
            for ltr2 in s :
                if lt2 in alp :
                    break
                if ltr1 == ltr2:
                    count+=1
                alp[ltr1] = count
        print(alp)
        return 0
4)49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = {}
        result= []

        for i,str1 in enumerate(strs):
            srt1 = sorted(str1)
            sub = []
            if str1 not in anaMap:
                anaMap[str(srt1)] = i
                for str2 in (strs) :
                    srt2 = sorted(str2)
                    if srt1 == srt2 :
                        sub.append(str2)
                    else:
                        continue
            else:
                continue
            result.append(sub)
