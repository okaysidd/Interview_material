"""
Valid Parenthesis String
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].
"""
class Solution:
	"""
	Creates two stacks that store opening bracket and star characters each.
	Closing brackets are compensated by popping from open brackets' stack,
	or from star stack.
	At the end, and open brackets left in the open stack are compensated
	with the stars in the stars stack. If any place brackets don't match or
	star characters are unavailable to compensate, return False.
	"""
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if s[0] == ')':
            return False
        i = 0
        open = []
        star = []
        while i < len(s):
            if s[i] == '(':
                open.append(i)
            elif s[i] == ')':
                if len(open) > 0:
                    open = open[:-1]
                elif len(star) > 0:
                    star = star[:-1]
                else:
                    return False
            elif s[i] == '*':
                star.append(i)
            i += 1
        if len(open) == 0:
            return True
        if len(open) > 0 and len(star) > 0:
            i = len(open) - 1
            while i > -1:
                j = 0
                f = 0
                while j < len(star):
                    if star[j] > open[i]:
                        f = 1
                        del star[j]
                        del open[i]
                        break
                    j += 1
                if not f:
                    return False
                i -= 1
        if len(open) == 0:
            return True
        return False

# s = '(((**)'
# s = '(*))'
# s = '()()'
# s = "(*))"
# s = ')('
# s = ''
# s = '*'
s = '('
# s = '()'
# s = "((*)(*))((*"
# s = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
# s = '"((()))()(())(*()()())**(())()()()()((*()*))((*()*)"'
# s = ""
# s = "(*()"
# s = "(((******))"
a = Solution()
print(a.checkValidString(s))
