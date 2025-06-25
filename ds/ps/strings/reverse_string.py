# Reverse a String (Without Using Built-ins)
# Problem: Reverse a string without using built-in reverse functions.
#
# Solution:
class Solution:
    def reverse_string(self, str):
        chars = list(str)
        left , right = 0, len(chars) -1
        while left<right:
            chars[left],chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        rev_string = "".join(chars)
        return rev_string
if __name__ == "__main__":
    sol = Solution()
    rev = sol.reverse_string('hello')
    print(rev)
    string = "hello"
    print(string[::-1])

# Complexity:
#
# Time: O(n), where n is the string length, as we traverse half the string.
# Space: O(n), since we convert the string to a list for immutability handling.

