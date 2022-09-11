# largest sum subarray in O(n)

from typing import List
from tabulate import tabulate


def largestSubarraySum(arr: List[int]):
	"""
	Returns the largest contiguous subarray with the largest sum
	:param arr: array to analyze
	:return: contiguous subarray with the largest sum
	"""
	dp = [0] * len(arr)
	dp[0] = arr[0]
	largestSum = dp[0]

	for i in range(1, len(arr)):
		dp[i] = max(dp[i - 1] + arr[i], arr[i])
		largestSum = max(largestSum, dp[i])

	return largestSum


if __name__ == '__main__':
	tests = [
		[-2, 1, -3, 4, -1, 2, 1, -5, 4],
		[1],
		[5, 4, -1, 7, 8]
	]
	result = map(lambda test: [test, largestSubarraySum(test)], tests)
	print(tabulate(result, headers=['test', 'ans']))
