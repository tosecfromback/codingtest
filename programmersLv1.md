https://school.programmers.co.kr/learn/courses/30/lessons/134240?language=python3
 ```python
def solution(food):
    answer = ''
    answerback = ''
    for i in range(1, len(food)):
        if food[i] > 1 or i > 1:
            answer += (str(i) * (food[i] // 2))
        elif i == 1 and food[i] < 3:
            pass
    answerback = answer[::-1]
    answer += str(0)
    answer += answerback
    return answer
  ```
