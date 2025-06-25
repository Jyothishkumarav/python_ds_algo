# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned)

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
        revrese_sum = 0
        x = abs(x)
        while x > 0:
            digit = x % 10
            revrese_sum = revrese_sum * 10 + digit
            if revrese_sum > 2 ** 31 - 1 or revrese_sum < -2 ** 31:
                return 0
            x = x // 10
        return revrese_sum * sign

if __name__ == '__main__':
    sol = Solution()
    result = sol.reverse(120)
    print(result)