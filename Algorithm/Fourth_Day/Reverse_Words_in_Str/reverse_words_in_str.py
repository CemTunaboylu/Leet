# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords_list(self, s: str) -> str:
        l = len(s)
        if l<2:
            return 
        
        c = 0
        s_list = []
        left = 0
        for i in range(l):
            if s[i] == " ":
                part = s[left:left+c]
                s_list.append(part[::-1])
                c = 0
                left = i+1
            else:
                c += 1
                
        part = s[left:left+c]
        s_list.append(part[::-1])
        return " ".join(s_list)

    def reverseWords_concat(self, s: str) -> str:
        l = len(s)
        if l<2:
            return 
        
        n_s = ""
        left = 0
        for i in range(l):
            if s[i] == " ":
                n_s += s[left:i][::-1] + " "
                left = i+1

        n_s += s[left:][::-1]
        return n_s
            

def test():
    s = "Let's take LeetCode contest"
    o = "s'teL ekat edoCteeL tsetnoc"

    sol = Solution()
    r_l = sol.reverseWords_list(s)
    r_s = sol.reverseWords_concat(s)
    assert r_l == r_s
    assert o == r_l

        
test()
        
