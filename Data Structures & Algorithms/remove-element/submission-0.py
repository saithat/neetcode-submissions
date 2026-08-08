class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while (j < len(nums)):
            if nums[i] == val:
                while (j < len(nums)):
                    if nums[j] == val:
                        j += 1
                    else:
                        break
                if j >= len(nums):
                    break
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
            i += 1
            j += 1
        return i
