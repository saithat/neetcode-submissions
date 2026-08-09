class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr)-1
        maxNum = arr[i]
        arr[i] = -1
        i -= 1
        while (i >= 0):
            tmp = maxNum
            if arr[i] > maxNum:
                maxNum = arr[i]
            arr[i] = tmp
            i -= 1
        return arr
            
