import random
import re
def caculator(s):
    formula00 = s
    formula01 = ''
    for i in formula00:
        if i.isspace():
            pass
        else:
            formula01 += i
    num01 = ''
    num_list = [] #用来存储单独数字
    symbol = [] #用来存储运算符号
    count = 0 #计数器，判断是否连续出现运算符
    for i in str(formula01):
        if count > 1:
            print('输入有误，请重新输入')
            break
        elif i.isdigit() or i == '.':
            num01 += i   #判断单个字符，对于连续的数字字符，将会组合在一起，即'789' 变为数字
            count = 0     #出现数字符号，计数器重置为0
        elif i == '*' or i == '/' or i == '+' or i == '-':
            num_list.append(float(num01))
            num01 = ''
            symbol.append(i)
            count += 1 #出现运算符，计数器加1，连续出现，count>1，第一个if条件生效
        else:
            print('输入有误，请重新输入')
            break
    num_list.append(float(num01))  #在公式最后不会出现运算符，所以需要将最后一个存入列表
    #对num_list和symbol两个列表进行处理，进行运算
    while symbol:
        while "*" in symbol or "/" in symbol: #先寻找*和/运算
            for i in symbol:
                if i == "*":
                    #找到运算符对应位置的symbol列表下标，对num_list里面对应位置的两个相邻数据进行运算，
                    # 并用结果覆盖原数据，同时删除symbol列表里的运算符
                    j = symbol.index("*")
                    result = num_list[j] * num_list[j+1]
                    del num_list[j:j+2]
                    num_list.insert(j,result)
                    symbol.remove("*")
                    break
                if i == "/":
                    j = symbol.index("/")
                    result = num_list[j] / num_list[j + 1]
                    del num_list[j:j + 2]
                    num_list.insert(j, result)
                    symbol.remove("/")
                    break
        while "+" in symbol or "-" in symbol:
            for i in symbol:
                if i == "+":
                    j = symbol.index("+")
                    result = num_list[j] + num_list[j+1]
                    del num_list[j:j + 2]
                    num_list.insert(j, result)
                    symbol.remove("+")
                    break
                if i == "-":
                    j = symbol.index("-")
                    result = num_list[j] - num_list[j + 1]
                    del num_list[j:j + 2]
                    num_list.insert(j, result)
                    symbol.remove("-")
                    break
    return num_list
def fangcheng():
    a=["+","-","*","/"]
    b=random.randint(1,100)
    c=random.randint(1,100)
    d=random.randint(1,100)
    e=random.randint(1,100)
    f=str(b)+random.choice(a)+str(c)+random.choice(a)+str(d)
    g=str(f)+'='+str(caculator(f)[0])
    h=str(b)+random.choice(a)+str(c)+random.choice(a)+str(d)+random.choice(a)+str(e)
    i=str(h)+'='+str(caculator(h)[0])
    cells=[g,i]
    j=random.choice(cells)
    m=re.findall( r"=(.+)",j )
    if float(m[0])%1==0:
        return j
    else:
        return fangcheng()
f = open("suanshuti.txt", 'w+')
for i in range(20):
    print(fangcheng(),file=f)







