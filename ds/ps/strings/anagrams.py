from collections import  defaultdict
class Solution:
    def is_anagram(self, string1: str, string2: str):
        if sorted(string1) == sorted(string2):
            return True
        return False
    def is_anagram_without_sort(self,string1: str, string2: str):
        if len(string1) != len(string2):
            return False
        char_count_dict = defaultdict(int)
        for c in string1:
            char_count_dict[c] = char_count_dict[c]+1
        for c1 in string2:
            if c1 in char_count_dict:
                char_count_dict[c1] = char_count_dict[c1] -1
                if char_count_dict[c1] == 0:
                    char_count_dict.pop(c1)
            else:
                return False
        if len(char_count_dict) == 0:
            return True
        return False



if __name__ == "__main__":
    sol = Solution()
    print(sol.is_anagram_without_sort("listen", "silent"))