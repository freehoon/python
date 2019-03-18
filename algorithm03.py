def inputNum():
    print("숫자 3개를 입력해 주세요")
    num = list()
    num.append(input("1번째 숫자 : "))
    num.append(input("2번째 숫자 : "))
    num.append(input("3번째 숫자 : "))
    return num

def inputNum2():
    print("숫자 3개를 입력해 주세요")
    num = list()
    num.append(input("1번째 숫자 : "))
    num.append(input("2번째 숫자 : "))
    num.append(input("3번째 숫자 : "))
    return num

def numCheck(num1, num2):
    s = 0
    b = 0
    o = 0
    idx1 = 0
    for n1 in num1:
        idx2 = 0
        for n2 in num2:
            if(n1 == n2 and idx1 == idx2):
                s += 1
            elif(n1 == n2 and idx1 != idx2):
                b += 1
            idx2 += 1
        idx1 += 1
        if(s == 3):
            print(" 3 Strike!!!!!!!")
            return s;
    print("S: {0}, B : {1}".format(s,b))
    print()


num1 = inputNum()

for idx in range(1, 10):
    print("{0}회!!!".format(idx))
    num2 = inputNum2()
    s = numCheck(num1, num2)
    if (s == 3):
        break