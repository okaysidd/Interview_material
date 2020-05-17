"""
Last Stone Weight
We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
Note:
1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""
class Solution:
    def lastStoneWeight(self, stones, sor=None):
        if len(stones) <= 1:
            try:
                return stones[0]
            except:
                return 0
        if sor == None:
            stones = sorted(stones, reverse=True)
        if stones[0] == stones[1]:
            return self.lastStoneWeight(stones[2:])
        else:
            new_num = abs(stones[0] - stones[1])
            stones = self.put(stones[2:], new_num)
            return self.lastStoneWeight(stones)
    def put(self, a, n):
        i = 0
        while i < len(a) and n>a[i]:
            i += 1
        a_l = a[:i]
        a_r = a[i:]
        a_l.append(n)
        a_l.extend(a_r)
        return a_l

a = Solution()
stones = [2,7,4,1,8,1]
print(a.lastStoneWeight(stones))