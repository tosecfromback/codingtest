def anyway1st(n):
    if  n % 2 == 0:
        a = 'hello'*(n // 2)
    elif n % 2 == 1:
        a = ('hello'*(n//2))+'world'
    answer = a
    return answer
x = int(input())
anyway1st(x)
