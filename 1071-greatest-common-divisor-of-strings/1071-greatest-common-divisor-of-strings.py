# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:  # Check if they have a common divisor pattern
            return ''
        
        g = gcd(len(str1), len(str2))  # Find GCD of the lengths
        return str1[:g]  # Return the common prefix of that length

        # len1= len(str1)
        # len2=len(str2)
        # def isdivisor(k):
        #     if len1%k or len2%k:
        #         return False
        #     f1,f2= len1//k, len2//k
        #     return str1[:k] * f1 == str1 and str2[:k] * f2 == str2

        # for i in range(min(len1,len2),0,-1):
        #     if isdivisor(i):
        #         return str2[:i]
        # return ''
        

        