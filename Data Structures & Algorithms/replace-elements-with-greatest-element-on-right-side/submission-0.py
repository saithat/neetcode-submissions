class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        for i in range(len(arr)):
            j = i+1
            maxNum = 0
            while (j < len(arr)):
                maxNum = arr[j] if arr[j] > maxNum else maxNum
                j += 1
            arr[i] = maxNum
        arr[i] = -1
        return arr
            
