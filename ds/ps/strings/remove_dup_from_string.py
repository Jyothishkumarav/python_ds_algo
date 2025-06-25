# Remove Duplicates from a String (Efficiently)
# Problem: Remove duplicate characters from a string, keeping the first occurrence.
#
# Solution:

class Solution:
    def remove_dup_from_string(self, string:str):
        unique_char = set()
        result = []
        for char in string:
            if char not in unique_char:
                unique_char.add(char)
                result.append(char)
        new_string = "".join(result)
        return new_string

    def set_intersection(self,s):
        return set(s) & set("aeiouAEIOU")

if __name__ == "__main__":
    sol = Solution()
    # print(sol.remove_dup_from_string(string="tree"))
    print(sol.set_intersection(s="atree"))
