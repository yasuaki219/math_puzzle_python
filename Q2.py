#def q2def(x, y):
#    return str(x) == str(y)[::-1]

#operator = ['+', '-', '*', '/', '']
operator = ['*', '']

for num in range(1000, 9999):
    if "0" in str(num):
       continue
    for i in operator:
        for j in operator:
            for k in operator:
                answer = str(num)[0] + i + str(num)[1] + j + str(num)[2] + k + str(num)[3]
                if len(answer) > 4:
                    if str(num) == str(eval(answer))[::-1]:
                        print(num, answer, str(eval(answer)))
