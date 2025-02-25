class Solution:
    def hammingWeight(self, n: int) -> int:
        """ bin(n) converts the number to binary representation as a string; how many 1's are in n """
        return bin(n).count('1')
