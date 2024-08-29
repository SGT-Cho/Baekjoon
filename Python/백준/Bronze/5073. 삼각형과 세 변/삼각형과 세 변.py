while True:
    A,B,C=map(int, input().split())
    K=[A,B,C]
    K.sort()
    if A==B==C==0:
        break
    elif A==B==C:
        print('Equilateral')
    elif(A==B or B==C or C==A)and(K[2]<K[0]+K[1]):
        print('Isosceles')
    elif(A!=B and B!=C and C!=A)and(K[2]<K[0]+K[1]):
        print('Scalene')
    else:
        print('Invalid')