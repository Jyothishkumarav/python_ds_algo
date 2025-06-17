# Product of Array Except Self
# Problem: Compute an array where each element is the product of all other elements, without using division.

class Solution:
    def product_array(self, arr:list):
        n = len(arr)
        result = []
        left_product = 1
        for index in range(n):
           result.append(left_product)
           left_product = left_product * arr[index]
        right_product = 1
        for index in range(n-1, -1,-1):
            result[index] = result[index] * right_product
            right_product *= arr[index]
        print(result)

if __name__ == "__main__":
    sol = Solution()
    sol.product_array([1, 2, 3, 4])