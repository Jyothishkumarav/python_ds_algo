# Sort 0s, 1s, and 2s (Dutch National Flag)
# Problem: Sort an array of 0s, 1s, and 2s in-place without using extra space or sorting functions.
#
# Solution:

class Solution:
    def sort_array(self, arr:list):
        low, mid, high = 0, 0 , len(arr) -1
        while mid<=high:
            if arr[mid] == 0:
                arr[low], arr[mid] == arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid+=1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -=1

if __name__ == "__main__":
    sol = Solution()
    arr = [2, 0, 2, 1, 1, 0]
    sol.sort_array(arr)
    print(arr)