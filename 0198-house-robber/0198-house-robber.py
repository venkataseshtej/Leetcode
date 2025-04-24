class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        elif n==2:
            return max(nums[1],nums[0])
        last_prev=nums[0]
        prev=max(nums[1],nums[0])
        for i in range(2, n):
            curr= max(prev, nums[i]+ last_prev)
            last_prev = prev
            prev= curr
            # dp[i]=max(dp[i-2],dp[i]+ dp[i-1])

        return curr
        