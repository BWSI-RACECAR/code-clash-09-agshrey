"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #9 - License Plate (licenseplate.py)


Author: Wonjun Lee

Difficulty Level: 5/10

Prompt: Jon was speeding on the highway with his RACECAR, and the highway camera has taken a picture 
of the RACECAR’s number plate. However, some characters on the plate are blurry. Please write a function 
that returns the number of possible combinations of the number plate. The number plate for his RACECAR
consists of 7 distinct characters, starting with 3 distinct alphabets and ending with 4 distinct numbers. 
The input will be passed as a string and any blurred characters will be written as ‘.’

Test Cases: 
Input: “ABC123.” ; Output: 7
Input: “.ON0123” ; Output: 24
Input: “.BC.234” ; Output: 168
"""

class Solution:
    def licensePlate(self,str):
        # type str: string
        # return: int
        
        # TODO: Write code below to return an int with the solution to the prompt
        # letterCount = 3-sum(c.isalpha() for c in str)
        # l = sum(c.isalpha() for c in str)
        # digitCount = 4-sum(c.isdigit() for c in str)
        # d = sum(c.isdigit() for c in str)
        # a = []
        # for s in str:
        #     if s == "." and letterCount != 0:
        #         a.append(26-l)
        #         letterCount += 1
        #         l+=1
        #     elif s == "." and digitCount != 0:
        #         a.append(10-d)
        #         digitCount+=1
        #         d+=1
        # total = 1
        # print(a)
        # for i in a:
        #     total *= i
        # return total
        d = sum(c.isdigit() for c in str)
        l = sum(c.isalpha() for c in str)
        letters = 26-l
        digits = 10-d
        a = []
        for b in range(d, 4):
            a.append(digits)
            digits -= 1
        for c in range(l, 3):
            a.append(letters)
            letters -= 1
        
        total = 1
        for i in a:
            total *= i
        return total
        

def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.licensePlate(string1)
    print(ans)

if __name__ == "__main__":
    main()