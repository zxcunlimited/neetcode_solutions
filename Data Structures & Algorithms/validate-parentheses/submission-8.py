class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
            else:
                if stack == []:
                    return False
                if bracket == ")" and stack[-1] =="(":
                    stack.pop()
                elif bracket == "]" and stack[-1] =="[":
                    stack.pop()
                elif bracket == "}" and stack[-1] =="{":
                    stack.pop()
                else:
                    return False
        if stack != []:
            return False
        return True