from math_lab import MathLab

if __name__ == "__main__":
    # just want to do something simple, for now get some inputs from user and do different operations with them
    
    math_lab = MathLab()    
        
    first_input = int(input("Please Enter the first number: "))
    second_input = int(input("Great! now enter the second number: "))

    print("addition of the numbers given is: " + str(math_lab.addition(first_input, second_input)))

    print("subtraction of the numbers given is: " + str(math_lab.subtraction(first_input, second_input)))
    
    print("division of the numbers given is: " + str(math_lab.division(first_input, second_input)))
    
    print("multiplication of the numbers given is: " + str(math_lab.multiplication(first_input, second_input)))
    
    print(str(first_input) + (" is prime and " if math_lab.isPrime(first_input) else " is not prime and ") + str(second_input) + (" is prime." if math_lab.isPrime(second_input) else " is not prime."))