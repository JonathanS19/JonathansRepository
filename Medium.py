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
