class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)
        c=Counter(nums)
        for i in c:
            if c[i]> math.floor(l/2):
                return i
        

        