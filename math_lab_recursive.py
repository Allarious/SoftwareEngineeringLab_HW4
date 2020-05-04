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
        def _mul(a, b, c=1):
            if a<c:
                return a, 0
            a, r = _mul(a, b + b, c + c)
            return (a - c, r + b) if a >= c else (a,r)
        return (_mul(a, b) if a<b else _mul(b, a))[1]
    
    def division(self, a, b):
        pass