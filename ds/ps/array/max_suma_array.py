class Solution:
    def max_sum(self, arr:list):
        current_sum = max_sum = arr[0]
        for num in arr[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(current_sum, max_sum)
        return max_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
