class Solution:
    def isValid(self, s: str) -> bool:
        parens = []
        for i in s:
            if i == ')':
                if not parens or parens.pop() != "(":
                    return False
            elif i == '}':
                if not parens or parens.pop() != "{":
                    return False
            elif i == ']':
                if not parens or parens.pop() != "[":
                    return False
            else:
                parens.append(i)
        if parens:
            return False
        return True