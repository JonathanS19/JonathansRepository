#Collection of solved leet code hard problems
1)
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        str_num = str(num)
        size = len(str_num)
        
        num_value = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 
    100: 'one hundred', 200: 'two hundred', 300: 'three hundred', 400: 'four hundred', 500: 'five hundred', 
    600: 'six hundred', 700: 'seven hundred', 800: 'eight hundred', 900: 'nine hundred', 
    1000: 'one thousand', 2000: 'two thousand', 3000: 'three thousand', 4000: 'four thousand', 
    5000: 'five thousand', 6000: 'six thousand', 7000: 'seven thousand', 8000: 'eight thousand', 9000: 'nine thousand'
}

        count = 0
        mod = 10
        wrd = ""
        
        for i in range(size):
            if i!= 0 :
                mod *= 10
                curr = num%mod
                prev = num%(mod/10)
                val = curr-prev
                wrd.join(num_value[val])
            else:
                curr = num%10
                wrd.join(num_value[curr])
        
        
        print(wrd)
        return 0
