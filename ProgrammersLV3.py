# billionmul
def solution(e, starts):
    num_list = [x+1 for x in range(e)]
    tmp_list = [x * y for x in num_list for y in num_list]
    mul_list = []
    answer = []
    cmp_list = [(0, 0)] * len(starts)
    for x in num_list:
        mul_list.append((x,tmp_list.count(x)))
    for x in range(0,len(starts)):
        for y in range(starts[x]-1, len(mul_list)):
            if cmp_list[x][1] < mul_list[y][1]:
                cmp_list[x] = mul_list[y]
            elif cmp_list[x][1] == mul_list[y][1] and cmp_list[x][0] < mul_list[y][0]:
                pass
        answer.append(cmp_list[x][0])

    return answer
