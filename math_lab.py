class MathLab():
    # this class is supposed to have some different mathmatical functions like sum, subtract...
    def addition(self, a, b):
        return a + b;
    
    def subtraction(self, a, b):
        return a - b;
    
    def division(self, a, b):
        return a/b;
    
    def multiplication(self, a, b):
        return a * b;
    
    def power(self, a, b):
        pass
    
    def isPrime(self, n):
        n = abs(int(n))
        if n < 2:
            return False
        if n == 2: 
            return True    
        if not n & 1: 
            return False
        for x in range(3, int(n**0.5)+1, 2):
            if n % x == 0:
                return False
        return True