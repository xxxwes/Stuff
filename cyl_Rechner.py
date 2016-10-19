def calc(a, b, rz):

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


def main():  # Wrapper function

    a = int(input('Erste Zahl: '))
    b = int(input('Zweite Zahl: '))
    rz = input(
        'Was für eine Rechnung möchtest du durchfuehren?\
        \nWaehle zwischen "+, -, *, /" : ')

    print(calc(a, b, rz))

if __name__ == '__main__':
    main()