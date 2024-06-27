def value(string):
    #print("value is == ",string,end = " ")
    if string == "-":
        value = 1
    elif string == "+":
        value = 1
    elif string == "*":
        value = 2
    elif string == "/":
        value = 3
    return value

def operator_compare(stack,string,list1):
    if len(stack) == 0:
        stack.append(string)
    else:
        if stack[-1] == "(":
            stack.append(string)
        elif value(string) > value(stack[-1]):
            stack.append(string)
        elif value(string) <= value(stack[-1]):
            for opr in stack[-1::-1]:
                if opr == '(':
                    stack.pop()
                    break
                list1.append(opr)
                stack.pop()
            stack.append(string)

def converting(infix):
    postEXP = []
    stack = []
    list1 = []

    for string in infix:
        if string.isalnum() == True:
            postEXP.append(string)

        elif string in "[{(":
            stack.append(string)

        elif string in "+-*/":
            operator_compare(stack,string,list1)
            if len(list1) > 0:
                postEXP.extend(list1)


        elif string in "]})":
            if string == ")":
                for opr in stack[-1::-1]:
                    if opr == '(':
                        stack.pop()
                        break
                    postEXP.append(opr)
                    stack.pop()
            elif string == "]":
                for opr in stack[-1::-1]:
                    if opr == '[':
                        stack.pop()
                        break
                    postEXP.append(opr)
                    stack.pop()
            elif string == "}":
                for opr in stack[-1::-1]:
                    if opr == '}':
                        stack.pop()
                        break
                    postEXP.append(opr)
                    stack.pop()
    
    if len(stack) > 0:
        for opr in stack[-1::-1]:
            postEXP.append(opr)
            stack.pop()
    print(postEXP)


string = #enter the expression here 
converting(string)
