seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos podem formar um triângulo ', end='')
    if seg1 == seg2 == seg3:
        print('equilátero!')
    elif seg1 != seg2 and seg2 != seg3 and seg1 != seg3:
        print('escaleno!')
    else:
        print('isósceles!')
else:
    print('Os segmentos NÃO podem formar um triângulo.')
