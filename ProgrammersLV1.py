#01st  https://school.programmers.co.kr/learn/courses/30/lessons/120802
def solution(num1, num2):
    if -50000 <= num1 <= 50000:
        if -50000 <= num2 <= 50000:
            answer = num1 + num2
    return answer
  
#02nd  https://school.programmers.co.kr/learn/courses/30/lessons/120803
def solution(num1 : int , num2 : int):
    answer = num1 - num2
    return answer

#03rd  https://school.programmers.co.kr/learn/courses/30/lessons/120804
def solution(num1, num2):
    answer = num1 * num2
    return answer
  
#04th  https://school.programmers.co.kr/learn/courses/30/lessons/120805
def solution(num1, num2):
    answer = num1 // num2
    return answer
  
#05th  https://school.programmers.co.kr/learn/courses/30/lessons/120806
def solution(num1, num2):
    answer =  int((num1 / num2) * 1000)
    return answer

#06th  https://school.programmers.co.kr/learn/courses/30/lessons/120807
def solution(num1, num2):
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer
  
#07th  https://school.programmers.co.kr/learn/courses/30/lessons/120808
def solution(numer1, denom1, numer2, denom2):
    tmp1, tmp2 = denom1, denom2
    numer1, denom1 = numer1*tmp2, denom1* tmp2
    numer2, denom2 = numer2*tmp1, denom2*tmp1
    tmp1 = numer1 + numer2
    tmp2 = denom2
    tmp3 = denom1
    for i in range(min(tmp1, tmp2),0, -1):
        if (tmp1 % i) == 0 and (tmp2 % i) == 0:
            tmp3 = i
            break
    tmp1 = tmp1 / tmp3
    tmp2 = denom1 / tmp3
    answer = [int(tmp1), int(tmp2)]
    return answer

#08th  https://school.programmers.co.kr/learn/courses/30/lessons/120809
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        answer.append(numbers[i]*2)
    return answer

#09th  https://school.programmers.co.kr/learn/courses/30/lessons/120810
def solution(num1, num2):
    answer = num1 % num2
    return answer

#10th  https://school.programmers.co.kr/learn/courses/30/lessons/120811
def solution(array):
    for i in range(len(array)):
        for x in range(i+1, len(array)):
            if array[i] > array[x]:
                array[i], array[x] = array[x], array[i]
    y = int(len(array) // 2)
    answer = array[y]
    return answer

#11th  https://school.programmers.co.kr/learn/courses/30/lessons/120812
def solution(array):
    most_num = 0
    most_count = 0
    if len(array) > 1:
        for i in range(len(array)):
            if array[i] != most_num:
                if most_count < array.count(array[i]):
                    most_count = array.count(array[i])
                    most_num = array[i]
                    answer = most_num
                elif most_count == array.count(array[i]):
                    answer = -1
    elif len(array) == 1:
        answer = array[0]
    return answer

#12th  https://school.programmers.co.kr/learn/courses/30/lessons/120813
def solution(n):
    answer = []
    for i in range(0, n+1, 1):
        if i % 2 == 1:
            answer.append(i)
    return answer


#13th  https://school.programmers.co.kr/learn/courses/30/lessons/120814
def solution(n):
    if n <= 7:
        answer = 1
    elif n > 7 and (n % 7) == 0:
        answer = (n // 7)
    elif n > 7 and (n % 7) != 0:
        answer = (n // 7) + 1
    return answer

#14th  https://school.programmers.co.kr/learn/courses/30/lessons/120815
def solution(n):
    for i in range(1, (n * 6)+1):
        if i % n == 0 and i % 6 == 0:
            answer = (i // 6)
            break
    return answer

#15th  https://school.programmers.co.kr/learn/courses/30/lessons/120816
def solution(slice, n):
    for i in range(1, (slice*n)+1):
        if slice*i >= n:
            answer = i
            break
    return answer
#16th  https://school.programmers.co.kr/learn/courses/30/lessons/120817
def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        answer = answer + numbers[i]
    answer = answer / len(numbers)
    return answer
