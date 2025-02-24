class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # Initialize an empty hashmap to store the indices of numbers encountered during the iteration

        """ Iterating through the list """
        for i, num in enumerate(nums):
            # Checking for complementary pair
            if target - num in hashmap:
                # Returning the result
                return [i, hashmap[target - num]]
            # Storing the indices
            hashmap[num] = i
