def resultChk(processes):
    cnt = 0
    for i in range(len(processes)):
        if processes[i] >= 100:
            cnt += 1
        else:
            break
    return cnt


processes = [93, 30, 55]
speeds = [1, 30, 5]
result = []

while True:
    for i in range(len(processes)):
        if processes[i] < 100:
            processes[i] = processes[i] + speeds[i]

    if processes[0] >= 100:
        checkCount = resultChk(processes)
        result.append(checkCount)
        for j in range(checkCount):
            processes.pop(0)
            speeds.pop(0)

    if len(processes) <= 0:
        print(result)
        break





###########################
# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]
#
