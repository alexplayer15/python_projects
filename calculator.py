def calculator():

    result = 0
    while True:
        try:
            number = float(input("Please enter a number:"))

        except ValueError:
            print('That is not a number, please try again.')
            continue

    
        operation = input('Please enter an operator of (+,-,*,/.) or type exit to leave.')

        if operation == 'exit':
            break
        
        if  operation not in ['+','-','*','/']:
            print('That is not a valid operator, please try again.')
            continue

        if operation == '+':
            result += number
        
        elif operation == '-':
            result -= number 
        
        elif operation == '*':
            result *= number 
        
        elif operation == '/':
            if result == 0:
                print('You cannot divide by 0')
            else: 
                result /= 0
        
        print(f'Result: {result}')

    print(f'Final Result: {result}')


    


calculator()




