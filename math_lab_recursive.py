class MathLabRecursive():
    def addition(self, a, b):
        if a == 0:
            return b
        return self.addition(a - 1, b + 1)
    
    def subtraction(self, a, b):
        if b == 0:
            return a
        return self.subtraction(a - 1, b - 1)
    
    def multiplication(self, a, b):
        
    
    def division(self, a, b):
        pass