from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = Counter(arr)
        len_a= len(a)
        # b=set()
        b= set(a.values())
        # for i in range(len(a)):
        #     b.add(a[i][1])
        if len_a ==len(b):
            return True
        else:
            return False


        