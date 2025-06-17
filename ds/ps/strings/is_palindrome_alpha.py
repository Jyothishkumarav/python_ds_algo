# Check if a String is a Palindrome
# Problem: Determine if a string reads the same forward and backward.

class Solution:
    def is_palindrome(self, string: str):
        chars = [c.lower() for c in string if c.isalnum()]
        left , right = 0, len(chars) -1
        while left < right:
            if chars[left] != chars[right]:
                return False
            left +=1
            right -=1
        return True
if __name__ == "__main__":
    sol = Solution()
    is_apl = sol.is_palindrome('A man, a plan, a canal: Panama')
    print(is_apl)

# Complexity:
#
# Time: O(n), where n is the string length, for cleaning and checking.
# Space: O(n) for the cleaned string.
