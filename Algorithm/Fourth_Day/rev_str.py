from typing import List
def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            e = len(s)-i-1	
            t = s[i]
            s[i] = s[e]
            s[e] = t


def test(s):
	a = "".join(s)
	reverseString(s, s)
	
	assert list(a[::-1]) == s

if __name__ == "__main__":

	s = ["h","e","l","l","o"]
	test(s)

	s = ["h"]
	test(s)

	s = ["a" , "b", "a", "b"]
	test(s)
