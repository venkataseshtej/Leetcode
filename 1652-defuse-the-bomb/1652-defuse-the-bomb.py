class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k<0:
            k=abs(k)
            code=code[::-1]
            n=len(code)
            x = code + code[:k]
            for i in range(n):
                code[i] = sum(x[i+1:i+k+1])
            return code[::-1]
        else:

            n=len(code)
            x = code + code[:k]
            for i in range(n):
                code[i] = sum(x[i+1:i+k+1])
            return code


        