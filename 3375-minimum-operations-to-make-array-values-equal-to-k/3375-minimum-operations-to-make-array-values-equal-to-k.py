class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a=set()
        for i in nums:
            if i < k:
                return -1
            elif i> k:
                a.add(i)
        return len(a)


        