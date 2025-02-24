""" Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. """
# XOR is a bitwise operator that compares corresponding bits of two numbers, producing 1 when different and 0 when they are the same.

Class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for num in nums:
      result ^= num # XOR (Exclusive Or) each number with the result
    return result

# The time complexity is O(n) because we go through the array once, where n is the number of elements.
