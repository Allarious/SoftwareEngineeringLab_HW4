from math_lab import MathLab

if __name__ == "__main__":
    # just want to do something simple, for now get some inputs from user and do different operations with them
    
    math_lab = MathLab()    
        
    first_input = int(input("Please Enter the first number: "))
    second_input = int(input("Great! now enter the second number: "))

    print(math_lab.sum(first_input, second_input))