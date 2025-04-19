class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=len(nums)
        s=[i for i in range(1,l+1)]
        return list(set(s) - set(nums))
        



        