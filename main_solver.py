pth = '(', ')'
opr = '^','*','/','+','-','.'
isSolved = False
onSolved = True

#VALIDITY CHECK
def valid_chk(eq, brkt):
    valid = True
    for xn in range(brkt[0],brkt[1]):
        x = eq[xn]
        if xn == brkt[0]: #if in first digit
            if x in opr:
                if x == '-' or x == '+':
                    if eq[xn+1] == '-' or eq[xn+1] == '+':
                        pass
                    else:
                        valid = False
                else:
                    valid = False
        else:
            if x in opr:
                if eq[xn+1] in opr:
                    if eq[xn+1] == '-' or eq[xn+1] == '+':
                        pass
                    else:
                        valid = False
    return valid

#BRACKET LOCATOR
def find_brkt(eq, valid):
    brkt = [0, len(eq)]
    haveO = False
    haveC = False
    for xn in range(len(eq)):
        if eq[xn] == '(':
            brkt[0] = xn + 1
            haveO = True
    if haveO:
        for xn in range(brkt[0],len(eq)):
            if eq[xn] == ')':
                brkt[1] = xn - 1
                valid = True
                break
            valid = False 
    return brkt, valid

#CHECK AROUND
def chk_around(eq, xn):
    #Find a in left
    a = ''
    b = ''
    a_neg = False
    b_neg = False
    d_pos = [0,len(eq)]
    for lfn in range(xn-1,-1,-1):
        lf = eq[lfn]
        if lf in opr or lf in pth:
            if lf == '.':
                a = lf + a 
            else:
                if lf == '-':
                    if eq[lfn-1] in opr or lfn == 0:
                        a_neg = True
                        d_pos[0] = lfn
                        break
                d_pos[0] = lfn + 1
                break
        else:
            if lf == ' ':
                    pass
            else:
                a = lf + a
    if (len(eq)+1) - (xn+1) == 1: #if right is last single digit
        b = eq[xn+1]
    else:
        for rtn in range(xn+1, len(eq)):
            rt = eq[rtn]
            if rt in opr or rt in pth:
                if rt == '.':
                    b = b + rt
                else:
                    if rtn == xn+1:
                        if rt == '-':
                            b_neg = True
                    else:
                        d_pos[1] = rtn
                        break
            else:
                if rt == ' ':
                    pass
                else:
                    b = b + rt
    a = float(a)
    b = float(b)
    if a_neg:
        a = - float(a)
    if b_neg:
        b = - float(b)
        d_pos[1] = d_pos[1]

    return a , b , d_pos
            
    
#SOLVE NOW
def solve_now(a, b, opr_val):
    if opr_val == '^':
        c = a**b
    elif opr_val == '*':
        c = a*b
    elif opr_val == '/':
        c = a/b
    elif opr_val == '+':
        c = a+b
    elif opr_val == '-':
        c = a-b
    return round(c, 5)

#EQ UPDATE
def update_eq(eq, c, d_pos):
    eql = list(eq)
    doneBrkt = False
    for _ in range(d_pos[0],d_pos[1]):
        eql.pop(d_pos[0])
    eql.insert(d_pos[0], str(c))
    if eql[d_pos[0]-1] == '(' and eql[d_pos[0]+1] == ')':
        eql.pop(d_pos[0]-1)
        eql.pop(d_pos[0])
        doneBrkt = True
    eq = ''
    for x in eql:
        eq = eq + x
    return eq, doneBrkt
    
        

#EXP
def opr_solve(eq, brkt, xn, opr_char):
    a, b, d_pos = chk_around(eq, xn)
    c = solve_now(a, b, opr_char)
    diff = (d_pos[1]-d_pos[0])- (len(str(c)))
    eq2, doneBrkt = update_eq(eq, c, d_pos)
    return eq2, diff, doneBrkt

def main_solve(eq, brkt, opr_char, isSolved):
    eq2 = eq
    stp = brkt[1]
    x = 0
    onSolve = True
    opr_count = 0
    valid = True
    diff = 0
    doneBrkt = False
    while onSolve:
        brkt = [0,len(eq2)]
        brkt, valid = find_brkt(eq2, valid)
        if diff == 0:
            stp = brkt[1]
        else:
            stp = brkt[1] - diff
        #VALID CHECK
        if valid:
            valid = valid_chk(eq2, brkt)
        else:
            print('INVALID')
            return eq2, isSolved, onSolve
        for xn in range(brkt[0], brkt[1]):
            if eq2[xn] == opr_char: #find last
                if xn == brkt[0]:
                    break
                opr_count += 1
                x_pos = xn #location of last
                
        if opr_count == 0: #if no opr
            onSolve = False
        else:
            opr_count = 0
            eq2, diff, doneBrkt = opr_solve(eq2, brkt, x_pos, opr_char)
            if doneBrkt:
                break
    solved = 0
    for xn in range(0, len(eq2)):
        x = eq2[xn]
        if x in opr:
            if xn == 0:
                if x == '-':
                    pass
                else:
                    solved +=1
            else:
                if x == '.':
                    pass
                else:
                    solved +=1
    if solved == 0:
        isSolved = True
    return eq2, isSolved, onSolve, doneBrkt
'''
print('Equation Solver v0.1\n')
eq = input('Your equation: \n')
brkt = [0,len(eq)]
while not isSolved:
    for opr_char in opr:
        if opr_char != '.':
            eq, isSolved, onSolve, doneBrkt = main_solve(eq, brkt, opr_char, isSolved)
            if doneBrkt:
                break
            if isSolved:
                print(f'Answer: {eq}')
                break
'''            
def remote_solve(eq):
    pth = '(', ')'
    opr = '^','*','/','+','-','.'
    isSolved = False
    onSolved = True
    brkt = [0,len(eq)]
    while not isSolved:
        for opr_char in opr:
            if opr_char != '.':
                eq, isSolved, onSolve, doneBrkt = main_solve(eq, brkt, opr_char, isSolved)
                if doneBrkt:
                    break
                if isSolved:
                    print(f'Answer: {eq}')
                    break
    return eq


                
    
