def arithmetic_arranger(problems, answer = False):
    firstline = []
    secondline = []
    dashline = []
    answerline = []
    if len(problems) > 5:
        return'Error: Too many problems.'
    else:
        for problem in problems:
            firstnumber = 0
            secondnumber = 0
            operator = ''
            answers = 0
            space = 0
            flag = False
            for i in problem:
                if i not in '0123456789+-*/ ':
                    return 'Error: Numbers must only contain digits.'

            for i in problem:
                if i in '0123456789':
                    if flag == False:
                        firstnumber = firstnumber*10 + int(i)
                    else:
                        secondnumber = secondnumber*10 + int(i)

                elif i == ' ':
                    flag = True   
                elif i in '+-*/':
                    if i in '*/':
                        return "Error: Operator must be '+' or '-'."
                    else:
                        if i == '+':
                            operator = '+'
                        else:
                            operator = '-' 
            if operator == '+':
                answers = firstnumber + secondnumber
            else:
                answers = firstnumber - secondnumber
            if len(str(firstnumber)) > 4 or len(str(secondnumber)) > 4:
                return "Error: Numbers cannot be more than four digits."
            str_firstnumber = str(firstnumber)
            str_secondnumber = str(secondnumber)
            space = max(len(str_firstnumber),len(str_secondnumber)) + 2
            str_firstnumber = str(firstnumber).rjust(space)
            str_secondnumber = str(secondnumber).rjust(space-2)
            str_answer = str(answers).rjust(space)
            formatted_second_line = operator + ' ' + str_secondnumber
            firstline.append(str_firstnumber)
            secondline.append(formatted_second_line)
            dashline.append('-'*space)
            answerline.append(str_answer)
    arranged_problems = '    '.join(firstline) + '\n' + \
                        '    '.join(secondline) + '\n' + \
                        '    '.join(dashline)
    if answer:
        arranged_problems += '\n' + '    '.join(answerline)
    return arranged_problems


            
            
                   
                 

def main():
    print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
    print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
    print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
    print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
    print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
main()
