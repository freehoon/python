def solution(heights):
    answer = [0]*len(heights)
    for i in range(len(heights)):
        #print()
        #print("i : {0}".format(i))
        #if i == 0:
        #    answer
        #    #answer.append(0)
        j = i
        while j:
            j -= 1
            #print("heights-i-{0} : {1}".format(i, heights[i]))
            #print("heights-j-{0} : {1}".format(j, heights[j]))

            if heights[i] < heights[j]:
                answer[i] = j+1
                #answer.append(j+1)
                break
            #if j == 0:
            #    answer.append(0)
        #print("answer : {0}".format(answer))
    return answer

#[6,9,5,7,4]
#[3,9,9,3,5,7,2]
#[1,5,3,6,7,6,5]
print(solution([6,9,5,7,4]))
print(solution([3,9,9,3,5,7,2]))
print(solution([1,5,3,6,7,6,5]))