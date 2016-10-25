def rechn(a, b, rz):

    if len(rz) > 1 and rz in '++--//**':
        return 'Nur ein Rechenzeichen!'

    if len(rz) > 1 and rz not in '+-/*':
        return 'Nur Rechenzeichen gueltig: "+, -, *, /"!'

    if rz not in '+-/*':
        return 'Nur folgenede Rechenzeichen gueltig: "+, -, *, /"!'
    
    if rz == '+':
        return(str(a) + ' ' + rz + ' ' + str(b) + ' = ' + str(a + b))
    if rz == '-':
        return(str(a) + ' ' + rz + ' ' + str(b) + ' = ' + str(a - b))
    if rz == '*':
        return(str(a) + ' ' + rz + ' ' + str(b) + ' = ' + str(a * b))
    if rz == '/':
        return(str(a) + ' ' + rz + ' ' + str(b) + ' = ' + str(a / b))


def main():  

    a = int(input('Erste Zahl: '))
    b = int(input('Zweite Zahl: '))
    rz = input(
        'Was für eine Rechnung möchtest du durchfuehren?\
        \nWaehle zwischen "+, -, *, /" : ')

    print(rechn(a, b, rz))

    input()

if __name__ == '__main__':
    main()
