# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = dict()
        c = 0
        longest = 0
        for i,k in enumerate(s):
                if k not in letters.keys():
                        # print(f"{k}@{i} is not in dict")
                        letters[k] = i
                        c += 1
                else:
                        # print(f"{k}@{i} is in dict")
                        longest = max(longest, c)
                        letters[k] = i
                        # print(f"c:{c} updated to ", end="")
                        c -= (i - letters[k]) 
                        # print(f"c:{c}")

        return longest

s = Solution()
a = "abcabcbb"
r = s.lengthOfLongestSubstring(a)
print(r)


