class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        initial = 0
        max_s= 0
        for i in range(len(gain)):
            initial += gain[i]
            max_s = max(initial, max_s)
        return max_s
        