# Remove Duplicates from Sorted Array
# Problem: Remove duplicates from a sorted array in-place and return the length of the unique elements.
class Solution:
    def remove_duplicate(self, arr:list):
        write_index = 1
        for index in range(1,len(arr)):
            if arr[index] != arr[index -1]:
                arr[write_index] = arr[index]
                write_index +=1
        return write_index
