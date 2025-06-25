# Find the Missing Number from 1 to N
# Problem: Given an array of n-1 integers from 1 to n, find the missing number.
#
# Solution:

class Solution:
    def find_missing_number(self, arr:list, n:int):
        expected_sum =  n * (n +1)// 2
        acutal_sum = sum(arr)
        missing_num = expected_sum - acutal_sum
        return missing_num

if __name__ == "__main__":
    sol = Solution()
    print(sol.find_missing_number([1, 2, 4, 5, 6], 6))