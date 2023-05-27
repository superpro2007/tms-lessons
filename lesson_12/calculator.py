def input_int_number() -> int:
    while True:
        try:
            number = int(input("Vvedite celoe 4islo"))
            return number
        except ValueError as ex:
            print("Error:", ex)
            print("Try again")
            
# 4)
class CalculationExitException(Exception):
    pass


# 2)
def calculate(left: int, right: int, operation: str):
    if operation == '+':
        return left + right
    elif operation == '-':
        return left - right
    elif operation == '*':
        return left * right
    elif operation == '/':
        return left / right
    elif operation == '!':
        raise CalculationExitException()
    else:
        raise ValueError(f'operation is not support: {operation}')
    
# 3)
def main():
    while True:
        a = input_int_number()
        b = input_int_number() 
        op = input('input operation: ')
        try:
            result = calculate(a,b,op)
            print(result, end='\n\n')
        except CalculationExitException:
            print('Ending program')
            
            break

        except Exception as e:
            print(e, end='\n\n')
        
        
# 4)

    
if __name__ == '__main__':
    main()