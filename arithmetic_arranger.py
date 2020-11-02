def arithmetic_arranger(problems,est = False):
    #Create lists to append later
    allproblems = [] 
    results = []
    firstnum = []
    secondnum = []
    op = []
    length = []
    spacer = " "
    #Limit input to 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    for h in problems:
        # Split problems into usable parts
        parts = h.split(' ')
        firstnum.append(parts[0])
        secondnum.append(parts[2])
        op.append(parts[1])
  
    def set(list):
        return allproblems.append(list)
    
    set(firstnum)
    set(op)
    set(secondnum)

    allprobs = list(zip(firstnum, op, secondnum))
    # printall problems
    for i in op:
        if i == "+":
            pass
        elif i == "-":
            pass
        else:
            return "Error: Operator must be '+' or '-'."
            
    for i in allprobs:
        #Ensure problem has no more than four digits
        if len(i[0]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if len(i[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        #Ensure input is numerical
        try:
            a = int(i[0])
            b = int(i[2])
        except:
            return 'Error: Numbers must only contain digits.'
        #Ensure operator is + or -
        if i[1] == '+':
            sumtotal = a+b
            results.append(sumtotal)
        elif i[1] == '-':
            differencetotal = a-b
            results.append(differencetotal)
        else:
            return "Error: Operator must be '+' or '-'."
        length.append(max(len(i[0]), len(i[2])))
    
    allprobs = list(zip(firstnum, op, secondnum, results, length))
    set(results)
    set(length)

    part1 = ""  #First number
    part2 = ""  #Operator & second number
    dash = ""  #Dashes
    part3 = ""  #Solution 
    for i in allprobs:
        #format output with proper spacing
        part1 += "  " + i[0].rjust(i[4], spacer) + "    "
        part2 += i[1] + " " + i[2].rjust(i[4], spacer) + "    "
        dash += "-" * len("  " + i[0].rjust(i[4], spacer)) + "    "
        part3 += str(i[3]).rjust(len("-" * len("  " + i[0].rjust(i[4], spacer))), spacer) + "    "
    #Create one solution including results and one without
    if est == True:
        arranged_problems = (part1.rstrip()+"\n"+part2.rstrip()+"\n"+dash.rstrip()+"\n"+part3.rstrip())
    else:
        arranged_problems = (part1.rstrip() + "\n" + part2.rstrip() + "\n" + dash.rstrip())
    return arranged_problems
