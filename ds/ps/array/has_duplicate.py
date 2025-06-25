# Array Duplicates and Frequencies: Q28 - Check for Duplicates in an Array
# Problem: Determine if an array contains any duplicate elements.
class Solution:
    def has_duplicate_or_not(self, arr:list):
        if len(arr) != len(set(arr)):
            return False
        return True