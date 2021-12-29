class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
                return False
        letters = dict()
        taken = []
        
        for s in s1:
                add(letters, s)

        for i in range(len(s2)):
                s = s2[i]
                if s not in letters.keys():
                        if len(s2)-i < len(s1): # There is not enough room to form a perm.
                                return False
                        while len(taken) > 0:
                                add(letters,taken.pop(0))
                        taken.clear()
                        continue
                else:
                        while letters[s] == 0 and len(taken)>0:
                                add(letters,taken.pop(0))
                        if s in letters:
                                rem(letters, s)
                                taken.append(s)

                if len(taken) == len(s1):
                        return True

        return len(taken) == len(s1)
                    
def add(d, ch):
        if ch in d.keys():
                d[ch] += 1
        else:
                d[ch] = 1
def rem(d, ch):
        if ch in d.keys():
                d[ch] -= 1