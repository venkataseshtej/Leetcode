class Solution:
    def isValid(self, s: str) -> bool:
        d={')':'(','}':'{', ']':'['}
        stack=[]
        for i in s:
            if i not in d:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if stack[-1]== d[i]:
                        stack.pop()
                    else:
                        return False
        return stack==[]


        