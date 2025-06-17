# Move All Zeros to End
# Problem: Move all zeros to the end of the array while maintaining the relative order of non-zero elements, in-place.

class Solution:
    def move_zero(self, arr:list):
        if not arr:
            return []
        non_zero_index = 0
        for index in range(len(arr)):
            if arr[index] != 0:
                arr[non_zero_index], arr[index] = arr[index], arr[non_zero_index]
                non_zero_index += 1

