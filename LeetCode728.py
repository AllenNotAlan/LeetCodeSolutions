"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

"""

#My solution -> makes use of a previous solution I used for reversing an integer value.
class Solution(object):
    def selfDividingNumbers(self, left, right):
        
        results =[] #the list containing all self-dividing numbers
        for i in range(left, right+1):
            num = i
            digitsOfNum = [] #digits of i (or num) for later division
            while num >= 1:
                pop = int(num) % 10 #pop last digit of i (or num) to go into digitsOfNum list
                digitsOfNum.append(pop)
                num /= 10

            count = 0
            for elem in digitsOfNum:
                if elem == 0: #if digit is 0 then don't divide i (or num) with it (fixes division by zero error)
                    continue
                if i % elem == 0:
                    count += 1
                if count == len(digitsOfNum): #checks if all numbers inside i (or num) divides i.
                    results.append(i) #appends i to the results containing all self-dividing numebrs within the range given

        return results


    print(selfDividingNumbers(1, 1, 128))