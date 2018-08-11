i = 11

while True:

    if str(i) == str(i)[::-1] and format(i, 'b') == format(i, 'b')[::-1] and format(i, 'o') == format(i, 'o')[::-1]:
        break
    i += 2
print(i)
