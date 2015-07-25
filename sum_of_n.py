def sum_of_n(n):
    a = 0
    result = []     #  배열을 이쪽에 만드는걸 애먹었고
                    #  배열에 추가하는 append도 이때 앎
    if n > 0:
        for x in range(n+1):
            a += x
            result.append(a)
        return result
    elif n < 0:
        for y in range(0, n-1, -1):
            a += y
            result.append(a)
        return result
    else:
        return 0


n = input('n의 값은?')
n = int(n)
print(sum_of_n(n))
