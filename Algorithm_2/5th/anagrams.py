from collections import defaultdict, deque
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        letters = defaultdict(int)
        space = set()
        window = deque()
        start_indices = []

        if len(p) == 0 or len(s) < len(p):
                return []
        for c in p:
                letters[c] += 1
                space.add(c)
        
        for i,ch in enumerate(s):
                # print(f" ch:{ch}, letters:{letters}, window:{window} ")
                if not ch in space:
                        for c in window:
                                letters[c] += 1
                        window.clear()
                        continue

                while letters[ch] == 0 and len(window)>0: # letters[ch] should not be smaller than 0
                        a = window.popleft()
                        letters[a] += 1

                if letters[ch] > 0:
                        pop(letters, ch)
                        window.append(ch)

                if len(letters) == 0:
                        start_indices.append(i-len(p)+1)
        return start_indices

def pop(d, v):
        d[v] -= 1
        if d[v] == 0:
                del d[v]
        

if __name__ == "__main__":
        s = Solution()
        a = s.findAnagrams("cbaebabacd", "abc")
        assert [0,6] == a
        
