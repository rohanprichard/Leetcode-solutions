class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = [''] * n
        
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                arr[i-1] = 'FizzBuzz'
            elif i % 3 == 0:
                arr[i-1] = 'Fizz'
            elif i % 5 == 0:
                arr[i-1] = "Buzz"
            else:
                arr[i-1] = str(i)
                
        return arr