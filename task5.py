def twoStrings(str1, str2):
    a = 0

    for i in str1:
        if i in str2:
            a = a + 1

    if a == 0:
        print('NO')
    else:
        print('YES')
 
twoStrings('hi', 'world')
twoStrings('hello', 'world')
