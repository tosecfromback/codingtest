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
  
#08th  https://school.programmers.co.kr/learn/courses/30/lessons/120809
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        answer.append(numbers[i]*2)
    return answer
