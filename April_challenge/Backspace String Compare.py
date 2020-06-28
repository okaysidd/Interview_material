"""
Backspace String Compare
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:
Can you solve it in O(N) time and O(1) space?
"""
# implements stack, appends at the front and pops from the end
class Solution:
    def pop(self, arr):
        arr = arr[1:]
        return arr
    def push(self, arr, a):
        i = 0
        arr.append(None)
        for j in range(i-1,-1,-1):
            arr[j+1] = arr[j]
        arr[0] = a
        return arr
    def put_in_stack(self, N):
        arr = []
        for i in N:
            if i == '#':
                arr = self.pop(arr)
            else:
                arr = self.push(arr, i)
        return arr
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = self.put_in_stack(S)
        T = self.put_in_stack(T)
        if S == T:
            return True
        return False

a = Solution()
print(a.backspaceCompare('ab#c', 'ad#c'))

# implements stack too, appends at end and pops from front
class Solution1:
    def put_in_stack(self, N):
        arr = []
        for i in N:
            if i == '#':
                arr = arr[:-1]
            else:
                arr.append(i)
        return arr
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.put_in_stack(S) == self.put_in_stack(T)