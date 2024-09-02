1)1894. Find the Student that Will Replace the Chalk
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        while True :
            for i,val in enumerate(chalk):
                if k < val:
                    return i
                else:
                    k-=val
