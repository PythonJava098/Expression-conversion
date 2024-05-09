'''
An advanced converter which converts Infix to postFix expressions
'''
def prdn(inpt_op):                      #assigning values to the various operand
    if inpt_op == "+":
        value = 0
    elif inpt_op == "-":
        value = 1
    elif inpt_op == "*":
        value = 2
    elif inpt_op == "/":
        value = 3
    
    return value

def addPrdn(ele,stack,postExp):                     #function to add the operand acc. to precedence
    
    if len(stack) == 0 or stack[-1] == "(":       #adding while empty stack
        stack.append(ele)
    
    else:

        top = stack[-1]                         
        if prdn(ele) > prdn(top):                       #camparing operands using values defined in the operand function
            stack.append(ele)
        else:
            for index in range(len(stack)-1,-1,-1):         #appending all the stack final in case the operand has less predecessor
                ele1 = stack[index]
                if ele1 == "(":
                    continue
                postExp.append(ele1)
                stack.pop()
            stack.append(ele)


def convert(string):
    postExp = []            
    stack = []
    for ele in string:
        
        if ele.isnumeric() == True:            
            postExp.append(ele)

        elif ele.isnumeric() == False:

            if ele == "(":
                if len(stack) == 0:
                    stack.append(ele)
                else:
                    print('here')
                    for index in range(len(stack)-1,-1,-1):
                        ele1 = stack[index]
                        postExp.append(ele1)
                        stack.pop()
                    stack = []
                    stack.append(ele)


            elif ele == ")":
                if "(" == stack[0]:
                    for index in range(len(stack)-1,0,-1):
                        ele1 = stack[index]
                        postExp.append(ele1)
                    stack = []


            else:
                addPrdn(ele,stack,postExp)


    if len(stack) > 0:
        postExp.extend(stack[-1::-1])


    print(postExp)
    print("stack",stack)

def numOprSep(string):
    list1 = []
    str1 = ""
    for ele in string:
        if ele.isnumeric() == True:
            str1 += ele
        elif ele.isspace() == False:
            list1.append(str1)
            str1 = ""
            list1.append(ele)
    
    return list1


string = input("Enter String: ")
convert(numOprSep("456*56+562+236*65"))