"""
Validate IP Address
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.
IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;
Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.
IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).
However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.
Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.
Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
Input: "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
# NOTE: The solutions below are not foolproof methods for checking IPv4 or IPv6.
These only satisfy the conditions specified by the leetcode problem.
"""
import re
class Solution:
	"""
	Solution using re.
	"""
	chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
	patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
	
	chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
	patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

	def validIPAddress(self, IP: str) -> str:        
		if self.patten_IPv4.match(IP):
			return "IPv4"
		return "IPv6" if self.patten_IPv6.match(IP) else "Neither" 

class Solution2:
	"""
	String matching solution.
	"""
	def validIPAddress(self, IP: str) -> str:
		def checkIPv4(s):
			try:
				if str(int(s)) == s and 0 <= int(s) < 256:
					return True
			except:
				return False
		def checkIPv6(s):
			if len(s) > 4: return False
			try:
				if int(s, 16) >= 0 and s[0] != '-': # extra check for leetcode specific test case
					return True
			except:
				return False
		if IP.count(".") == 3 and all(checkIPv4(i) for i in IP.split(".")): 
			return "IPv4"
		if IP.count(":") == 7 and all(checkIPv6(i) for i in IP.split(":")): 
			return "IPv6"
		return "Neither"

IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
x = Solution()
print(x.validIPAddress(IP))
