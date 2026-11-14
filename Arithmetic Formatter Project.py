def arithmetic_arranger(problems, show_answers=False):
    digit = '0123456789'
    operator = '+-'
    result = ''
    operator_check = []
    operand_check = []
    flag1 = 0
    flag2 = 0
    flag3 = 0

    for i in range(len(problems)):
        operator_check.append(problems[i].split()[1])
        operand_check.append(problems[i].split()[0])
        operand_check.append(problems[i].split()[-1])
    
    for i in range(len(operand_check)):
        if len(operand_check[i]) > 4:
            flag1 += 1
        for n in range(len(operand_check[i])):
            if not operand_check[i][n] in digit:
                flag2 += 1
  
    for i in operator_check:
        if not i in operator:
            flag3 += 1
    
    if len(problems) > 5:
        return 'Error: Too many problems.'
    elif flag1 > 0:
        return 'Error: Numbers cannot be more than four digits.'
    elif flag2 > 0:
        return 'Error: Numbers must only contain digits.'
    elif flag3 > 0:
        return "Error: Operator must be '+' or '-'."
    elif show_answers == True:
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

        answer = []
        for i in range(len(problems)):
            operand1 = problems[i].split()[0]
            operand2 = problems[i].split()[-1]
            if '+' in problems[i]:
                operator = '+'
                answer.append(int(operand1) + int(operand2))
            else:
                operator = '-'
                answer.append(int(operand1) - int(operand2))

            if len(operand2) >= len(operand1):
                space2 = ' '
            else:
                space2 = (abs(len(operand1) - len(operand2)) + 1)*' '

            result += space1 + operator + space2 + operand2

            if i < len(problems) - 1:
                space1 = 4*' '
        
        result += '\n'
        space_answer = []

        for i in range(len(problems)):
            operand1 = problems[i].split()[0]
            operand2 = problems[i].split()[-1]
            if len(operand1) >= len(operand2):
                dash = '-'*(len(operand1) + 2)
            else:
                dash = '-'*(len(operand2) + 2)
            space_answer.append(' '*(len(dash) - len(str(answer[i]))))
            if i < 1:
                result += dash 
            else:
                result += 4*' ' + dash

        result += '\n'

        for i in range(len(problems)):
            if i < 1:
                result += space_answer[i] + str(answer[i])
            else:
                result += 4*' ' + space_answer[i] + str(answer[i])

        return result
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

            if len(operand2) >= len(operand1):
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
            if len(operand1) >= len(operand2):
                dash = '-'*(len(operand1) + 2)
            else:
                dash = '-'*(len(operand2) + 2)
            if i < 1:
                result += dash 
            else:
                result += 4*' ' + dash
        
        return result


print(arithmetic_arranger(["32 + 698"], True))




    








    

        

        
        
    
    
   

