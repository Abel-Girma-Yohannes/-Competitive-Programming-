class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        mylist = [] # create an empty list that will be filled it's length is = n 
        i = 1 # we start counting at one because the array is (1-indexed).
        while (i<=n):
            if i%3 == 0 and i%5 == 0 : # in-case both reminder only retrives zero if the number accepts the division by 3 or 5
                mylist.append('FizzBuzz')
            elif i%3 == 0: # in-case 3
                mylist.append('Fizz')
            elif i%5 == 0: #in-case 5
                mylist.append('Buzz')
            else: # if non of the above we append (push) the number as a string
                mylist.append(str(i))
            i+=1

        return mylist
