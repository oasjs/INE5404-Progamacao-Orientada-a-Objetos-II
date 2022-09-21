# Fibonacci, Fatorial, Fibonarial, Primo

class Series():

    def fibonacci(n:int):
        stop = n

        while stop > 0:
            if n <= 1:
                return n
            else:
                return (Series.fibonacci(n-1) + Series.fibonacci(n-2))


    def factorial(self, n:int):
        if n <= 1:
            return n
        else:
            return self.factorial(n)*self.factorial(n-1)

    def fibonarial():
        pass

    def prime():
        pass

print(Series.fibonacci(5))