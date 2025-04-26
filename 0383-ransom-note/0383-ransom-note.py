class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1= Counter(ransomNote)
        c2= Counter(magazine)

        for i in c1:
            if i not in c2:
                return False
            else:
                if c2[i] < c1[i]:
                    return False
        return True

        