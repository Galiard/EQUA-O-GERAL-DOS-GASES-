while True:
    print('''ME INFORME QUAL VALOR VOCÊ DESEJA SABER :
    [0] p1
    [1] v1
    [2] t1
    [3] p2
    [4] v2
    [5] t2''')
    escolha = ' '
    while escolha not in '012345':
        escolha = str(input(': ')).strip().upper()[0]
    if escolha == '0':
        print('Ok vamos descobrir o P1')
        print('-='*22)
        v1 = float(input('Digite o valor de v1 : '))
        t1 = float(input('Digite o valor de t1 : '))
        ck = ' '
        while ck not in 'SN':
            ck = str(input('Esse valor já está em Kelvin? ')).strip().upper()[0]
        if ck == 'N':
            t1 = t1+273
            print(f'Ok... converti o t1 para kelvin ele ficou assim {t1:.2f}k ...De nada boy')
        p2 = float(input('Digite o valor de p2 : '))
        v2 = float(input('Digite o valor de v2 : '))
        t2 = float(input('Digite o valor de t2 : '))
        ck = ' '
        while ck not in 'SN':
            ck = str(input('Esse valor já está em Kelvin? ')).strip().upper()[0]
        if ck == 'N':
            t2 = t2+273
            print(f'Ok... converti o t2 para kelvin ele ficou assim {t2:.2f}k ...De nada boy')
        soma1 = p2*v2
        soma2 = soma1*t1
        soma3 = v1*t2
        p1 = soma2/soma3
        print(f'O valor de p1 é {p1:.2f} ')
    elif escolha == '1':
        print('Ok vamos descobrir o V1')
        print('-='*22)
        p1 = float(input('Digite o valor de p1 : '))
        t1 = float(input('Digite o valor de t1 : '))
        ck = ' '
        while ck not in 'SN':
            ck = str(input('Esse valor já está em Kelvin? ')).strip().upper()[0]
        if ck == 'N':
            t1 = t1+273
            print(f'Ok... converti o t1 para kelvin ele ficou assim {t1:.2f}k ...De nada boy')
        p2 = float(input('Digite o valor de p2 : '))
        v2 = float(input('Digite o valor de v2 : '))
        t2 = float(input('Digite o valor de t2 : '))
        ck = ' '
        while ck not in 'SN':
            ck = str(input('Esse valor já está em Kelvin? ')).strip().upper()[0]
        if ck == 'N':
            t2 = t2+273
            print(f'Ok... converti o t2 para kelvin ele ficou assim {t2:.2f}k ...De nada boy')
        soma1 = p2*v2
        soma2 = soma1*t1
        soma3 = p1*t2
        v1 = soma2/soma3
        print(f'O valor de v1 é {v1:.2f} ')
    elif escolha == '2':
        p1 = float(input('Digite o valor de P1: '))
        v1 = float(input('Digite o valor de V1: '))
        p2 = float(input('Digite o valor de P2: '))
        v2 = float(input('Digite o valor de V2: '))
        t2 = float(input('Digite o valor de T2: '))
        ck = ' '
        while ck not in 'SN':
            ck = str(input('Esse valor já está em Kelvin? ')).strip().upper()[0]
        if ck == 'N':
            t2 = t2+273
            print(f'Ok... converti o t2 para kelvin ele ficou assim {t2:.2f}k ...De nada boy')
        soma1 = p1*v1
        soma2 = p2*v2
        soma3 = soma1*t2
        t1 = soma3/soma2
        print(f'O valor de T1 é {t1:.2f} ')
    elif escolha == '3':
        p1 = float(input('Me diga o valor de P1: '))
        v1 = float(input('Me diga o valor de V1: '))
        t1 = float(input('Me diga o valor de T1: '))
        ck = ' '
        while ck not in 'SN':
            ck = str(input('Esse valor já está em Kelvin? ')).strip().upper()[0]
        if ck == 'N':
            t1 = t1+273
            print(f'Ok... converti o t1 para kelvin ele ficou assim {t1:.2f}k ...De nada boy')
        v2 = float(input('Me diga o valor de V2: '))
        t2 = float(input('Me diga o valor de T2: '))
        ck = ' '
        while ck not in 'SN':
            ck = str(input('Esse valor já está em Kelvin? ')).strip().upper()[0]
        if ck == 'N':
            t2 = t2+273
            print(f'Ok... converti o t2 para kelvin ele ficou assim {t2:.2f}k ...De nada boy')
        soma1 = p1*v1
        soma2 = soma1*t2
        soma3 = v2*t1
        p2 = soma2/soma3
        print(f'O valor de P1 é: {p2:.2f} ')
    elif escolha == '4':
        p1 = float(input('Me diga o valor de P1: '))
        v1 = float(input('Me diga o valor de V1: '))
        t1 = float(input('Me diga o valor de T1: '))
        ck = ' '
        while ck not in 'SN':
            ck = str(input('Esse valor já está em Kelvin? ')).strip().upper()[0]
        if ck == 'N':
            t1 = t1+273
            print(f'Ok... converti o t1 para kelvin ele ficou assim {t1:.2f}k ...De nada boy')
        p2 = float(input('Me diga o valor de P2: '))
        t2 = float(input('Me diga o valor de T2: '))
        ck = ' '
        while ck not in 'SN':
            ck = str(input('Esse valor já está em Kelvin? ')).strip().upper()[0]
        if ck == 'N':
            t2 = t2+273
            print(f'Ok... converti o t2 para kelvin ele ficou assim {t2:.2f}k ...De nada boy')
        soma1 = p1*v1
        soma2 = p2*t1
        soma3 = soma1*t2
        v2 = soma3/soma2
        print(f'O valor de V2 é: {v2:.2f}')
    elif escolha == '5':
        p1 = float(input('Me diga o valor de P1: '))
        v1 = float(input('Me diga o valor de V1: '))
        t1 = float(input('Me diga o valor de T1: '))
        ck = ' '
        while ck not in 'SN':
            ck = str(input('Esse valor já está em Kelvin? ')).strip().upper()[0]
        if ck == 'N':
            t1 = t1+273
            print(f'Ok... converti o t1 para kelvin ele ficou assim {t1:.2f}k ...De nada boy')
        p2 = float(input('Me diga o valor de P2: '))
        v2 = float(input('Me diga o valor de V2: '))
        soma1 = p1*v1
        soma2 = p2*v2
        soma3 = soma2*t1
        t2 = soma3/soma1
        print(f'O valor de T2 é : {t2:.2f} ')
    print('-='*20)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja descobrir algo mais ? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Até mais')
        
        


        
        
