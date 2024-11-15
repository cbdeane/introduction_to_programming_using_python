def sumOfString(s):
    delta = ''
    sigma = 0
    for i in range(len(s)):
        if s[i].isdigit() or s[i] == '.':
            delta += s[i]
            print("current number in the works is " + delta)
        if s[i] == ',':
            print("adding" + delta)
            sigma += float(delta)
            delta = ''
        if s[i].isdigit() != True and s[i] != '.' and s[i] != ',':
            print('Invalid input')
            break
        if i == len(s)-1:
            sigma += float(delta)
            print("adding " + delta)
    print("The sum of the values is", sigma)
    return sigma

stringToSum = '1.23,2.4,3.123'
sumOfString(stringToSum)