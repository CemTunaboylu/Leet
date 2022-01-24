class Solution:
	def hammingWeight(self, n: int) -> int:
		m1 = 6148914691236517205  #b"0x5555555555555555"		
		m2 = 3689348814741910323 #b"0x3333333333333333"
		f4 = 1085102592571150095 #b"0x0f0f0f0f0f0f0f0f"
		f8 = 71777214294589695 #b"0x00ff00ff00ff00ff"
		f16 = 281470681808895 #b"0x0000ffff0000ffff"
		f32 = 4294967295 #b"0x00000000ffffffff"
		h1 = 72340172838076673 # b"0x0101010101010101"

		h = 127 # b"0x7f"
		
		n -= (n >> 1)&m1
		n = (n&m2)+((n>>2)&m2)
		n = (n + (n >> 4))&f4
		n += (n >> 8)
		n += (n >> 16)
		n += (n >> 32)

		return n & h #b"0x7f"

	def b_force(self, n):
		b = bin(n)[2:]
		c = 0
		for ch in b:
			c += (ch == 1)

		return c 
		
DEBUG = True
def test(n):
	s = Solution()
	r = s.hammingWeight(n)
	if DEBUG:
		print(f"Hamming Distance of {n} -> {bin(n)}, is {r}")
	c = bin(n).count("1")
	
	assert r == c

def speed_test():
	n = 2**20 - 1
	s = Solution()
	from time import time 
	now = time()
	for i in range(100):
		a = s.b_force(n)
	t1 = time()-now
	print(f"B_force took {t1}")
	now = time()
	for i in range(100):
		a = s.hammingWeight(n)
	t2 = time()-now
	print(f"Wiki took {t2}")

	print(f"Wiki is {t1/t2} times faster")
	
if __name__ == "__main__":
	#n = int(b"0110110010111010", 2)
	#test(n)
	#n = 2**16 - 1
	#test(n) 
	speed_test()



