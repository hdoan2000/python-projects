def arithmetic_arranger(problems, show_answers=False):
    digit = '0123456789+-'
    result = ''

    if len(problems) > 5:
        return 'Error: Too many problems.'
    elif '*' or '/' in problems:
        return "Error: Operator must be '+' or '-'."
    else:
        my_dict = {}
        
        for i in range(len(problems)):
            operand1 = problems[i].split()[0]
            operand2 = problems[i].split()[-1]

            if i < 1:
                if len(operand1) >= len(operand2):
                    if operand1 in my_dict:
                        my_dict[operand1].append('  ')
                    else:
                        my_dict[operand1] = []
                        my_dict[operand1].append('  ')
                        
                else: 
                    if operand1 in my_dict:
                        my_dict[operand1].append((abs(len(operand1) - len(operand2)) + 2)*' ')
                    else:
                        my_dict[operand1] = []
                        my_dict[operand1].append((abs(len(operand1) - len(operand2)) + 2)*' ')
            else:
                if len(operand1) >= len(operand2):
                    if operand1 in my_dict:
                        my_dict[operand1].append(6*' ')
                    else:
                        my_dict[operand1] = []
                        my_dict[operand1].append(6*' ')
                else:
                    if operand1 in my_dict:
                        my_dict[operand1].append((abs(len(operand1) - len(operand2)) + 6)*' ')
                    else:
                        my_dict[operand1] = []
                        my_dict[operand1].append((abs(len(operand1) - len(operand2)) + 6)*' ')

        for i in range(len(problems)):
            operand1 = problems[i].split()[0]
            if len(my_dict[operand1]) > 1:
                result += my_dict[operand1][0] + operand1
                my_dict[operand1].pop(0)
            else:
                result += my_dict[operand1][0] + operand1

        result += '\n'
        space1 = ''

        for i in range(len(problems)):
            operand1 = problems[i].split()[0]
            operand2 = problems[i].split()[-1]
            if '+' in problems[i]:
                operator = '+'
            else:
                operator = '-'

            if len(operand2) > len(operand1):
                space2 = ' '
            else:
                space2 = (abs(len(operand1) - len(operand2)) + 1)*' '

            result += space1 + operator + space2 + operand2

            if i < len(problems) - 1:
                space1 = 4*' '
        
        result += '\n'

        for i in range(len(problems)):
            operand1 = problems[i].split()[0]
            operand2 = problems[i].split()[-1]
            dash = '-'*(max(len(operand1), len(operand2)) + 2)
            result += dash + 4*' '
        
        return result

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))










    








    

        

        
        
    
    
   

