# coding=utf-8
def fn369(num):
    count = 0
    for i in range(1, num+1):
        strNum = str(i)
        for j in len(strNum):
            if int(strNum[j]) != 0 and (int(strNum[j]) % 3) == 0:
                count += 1

    answer = count
    return answer

num = input("입력 : ")
result = fn369(num)
print ("결과 : {0}".format(result))
