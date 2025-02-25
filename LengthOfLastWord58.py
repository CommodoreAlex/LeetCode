class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """ Strip the leading and trailing spaces """
        words = s.strip().split() 

        """ Return the length of the last word in the list """
        return len(words[-1]) if words else 0
