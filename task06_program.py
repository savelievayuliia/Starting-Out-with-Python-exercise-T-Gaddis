coeff1 = 9/5
coeff2 = 32
print("T in Celcius\tT in Farenheit")
for c in range (0,21,1):
    f = coeff1*c+coeff2
    print(c,"\t",format(f,".1f"))