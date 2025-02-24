class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [] # Expected output calls for a string array

        # Logic to move the program forward
        for i in range(1, n + 1):   
            # Checks
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i)) # As a string, if none of the above conditions are true
        return answer # Returning the string array.
