import math
import cmath

def calculator():
    print("Welcome to Advanced Calculator")
    print("Operations available:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Square root (sqrt)")
    print("7. Logarithm (log)")
    print("8. Trigonometric functions (sin, cos, tan)")
    print("9. Complex numbers (support basic +,-,*,/ operations)")
    print("10. Exit")

    while True:
        choice = input("\nEnter the number for the operation you want to perform (or 'exit' to quit): ")
        
        if choice == '10' or choice.lower() == 'exit':
            print("Exiting Calculator. Goodbye!")
            break
        
        try:
            if choice in ['1', '2', '3', '4', '5']:
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))
                
                if choice == '1':
                    print("Result:", x + y)
                elif choice == '2':
                    print("Result:", x - y)
                elif choice == '3':
                    print("Result:", x * y)
                elif choice == '4':
                    if y == 0:
                        print("Error: Cannot divide by zero.")
                    else:
                        print("Result:", x / y)
                elif choice == '5':
                    print("Result:", math.pow(x, y))

            elif choice == '6':
                x = float(input("Enter the number for square root: "))
                print("Result:", math.sqrt(x) if x >= 0 else cmath.sqrt(x))
            
            elif choice == '7':
                x = float(input("Enter the number for logarithm: "))
                base = float(input("Enter the base (default is 'e' for natural log): ") or math.e)
                if x > 0 and base > 0:
                    print("Result:", math.log(x, base))
                else:
                    print("Error: Logarithm requires positive arguments.")

            elif choice == '8':
                angle = float(input("Enter the angle in degrees: "))
                radian = math.radians(angle)
                trig_choice = input("Choose function (sin, cos, tan): ").lower()
                
                if trig_choice == 'sin':
                    print("Result:", math.sin(radian))
                elif trig_choice == 'cos':
                    print("Result:", math.cos(radian))
                elif trig_choice == 'tan':
                    print("Result:", math.tan(radian) if math.cos(radian) != 0 else "Error: Undefined (cosine is zero)")
                else:
                    print("Error: Invalid trigonometric function.")

            elif choice == '9':
                complex_str1 = input("Enter the first complex number (e.g., '1+2j'): ")
                complex_str2 = input("Enter the second complex number (e.g., '3+4j'): ")
                complex1 = complex(complex_str1)
                complex2 = complex(complex_str2)
                op = input("Enter the operation (+, -, *, /): ")
                
                if op == '+':
                    print("Result:", complex1 + complex2)
                elif op == '-':
                    print("Result:", complex1 - complex2)
                elif op == '*':
                    print("Result:", complex1 * complex2)
                elif op == '/':
                    print("Result:", complex1 / complex2 if complex2 != 0 else "Error: Cannot divide by zero.")
                else:
                    print("Error: Invalid operation for complex numbers.")
                    
            else:
                print("Error: Invalid operation selection.")
        
        except ValueError:
            print("Error: Invalid input, please enter numeric values where required.")
        except Exception as e:
            print("An unexpected error occurred:", str(e))

calculator()