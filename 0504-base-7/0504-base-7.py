class Solution:
    def convertToBase7(self, num: int) -> str:
        if num ==0:
            return '0'
        original_num = num
        num = abs(num)
        remainders =[]
        while num >0:
            remainder = num %7
            remainders.append(str(remainder))
            num = num//7
        if original_num <0:
            remainders.append('-')
        remainders = reversed(remainders)
        return ''.join(remainders)


        