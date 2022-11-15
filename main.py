sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
sides = sorted(sides, reverse=True)
smax = 0
for i in range(len(sides)):
    for j in range(i + 1, len(sides)):
        for k in range(j + 1, len(sides)):
            a = sides[i]
            b = sides[j]
            c = sides[k]
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
                s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
                if s > smax:
                    smax = s
print("Максимальная площадь треугольника", smax)


#Домашняя работа:
a= float(input())
b= float(input())
c= float(input())
D=b**2-4*a*c  #дискриминант
print ('дискриминант',D**0.5)
if D>0:
    print ('x1=',((-b+D**0.5)/(2*a)),'x2=',((-b-D**0.5)/(2*a)))
elif D==0:
    print (-b/(2*a))
else :
    print ('нет корней')