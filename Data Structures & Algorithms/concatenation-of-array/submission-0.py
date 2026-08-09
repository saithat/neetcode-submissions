class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lenNums = len(nums)
        ans = [0] * 2 * lenNums
        for i, n in enumerate(nums):
            ans[i] = n
            ans[i+lenNums] = n
        return ans