# longest palindromic substring in O(n)

from tabulate import tabulate


def longestPalindrome(s: str) -> str:
	"""
	Returns the longest palindromic substring
	:param s: string to analyze
	:return: longest palindromic substring
	"""
	if s == s[::-1]: return s
	return max(
		longestPalindrome(s[1:]),
		longestPalindrome(s[:-1]),
		key=len
	)


if __name__ == '__main__':
	tests = [
		'babad',
		'babab',
		'babbada',
		'banana'
	]
	result = map(lambda test: [test, longestPalindrome(test)], tests)
	print(tabulate(result, headers=['test', 'longestSubPalindrome']))

"""
O(n) method is called "Manacher’s Algorithm"
"""
