print("\033[1;32m    Считатель денег")
a=int(input("\033[1;33m Купюры 1000: \033[0;0m"))
b=int(input("\033[1;33m Купюры 2000: \033[0;0m"))
c=int(input("\033[1;33m Купюры 5000: \033[0;0m"))
d=int(input("\033[1;33m Купюры 5000 №2: \033[0;0m"))
e=int(input("\033[1;33m Купюры 10000: \033[0;0m"))
f=int(input("\033[1;33m Купюры 10000 №2: \033[0;0m"))
g=int(input("\033[1;33m Купюры 20000: \033[0;0m"))
h=int(input("\033[1;33m   Монеты 500: \033[0;0m"))
i=int(input("\033[1;33m   Монеты 200: \033[0;0m"))
j=int(input("\033[1;33m   Монеты 100: \033[0;0m"))
k=int(input("\033[1;33m   Монеты 50: \033[0;0m"))
a2=(a*1000)
b2=(b*2000)
c2=(c*5000)
d2=(d*5000)
e2=(e*10000)
f2=(f*10000)
g2=(g*20000)
h2=(h*500)
i2=(i*200)
j2=(j*100)
k2=(k*50)
S=(a2+b2+c2+d2+e2+f2+g2+h2+i2+j2+k2)
Sk=(a2+b2+c2+d2+e2+f2+g2)
Sm=(h2+i2+j2+k2)
print("\033[1;32m    Итог")
print("\033[1;35m   Купюры 1000: ",a,"-->",a2)
print("   Купюры 2000: ",b,"-->",b2)
print("   Купюры 5000: ",c,"-->",c2)
print("   Купюры 5000 №2:",d,"-->",d2)
print("   Купюры 10000: ",e,"-->",e2)
print("   Купюры 10000 №2:",f,"-->",f2)
print("   Купюры 20000: ",g,"-->",g2)
print("     Монеты 500: ",h,"-->",h2)
print("     Монеты 200: ",i,"-->",i2)
print("     Монеты 100: ",j,"-->",j2)
print("     Монеты 50: ",k,"-->",k2,"\033[0;0m")
print("\033[1;36m Общий: \033[0;0m",S)
print("\033[1;36m Купюры: \033[0;0m",Sk)
print("\033[1;36m Монеты: \033[0;0m",Sm)
javoblar = {
    'javob1' : '144',
    'javob2' : '210',
    'javob3' : '162',
    'javob4' : '546',
    'javob5' : '720',
    'javob6' : '525',
    'javob7' : '168',
    'javob8' : '475',
    'javob9' : '2968',
    'javob0' : '31059'
}
savollar = ['6*24', '6*35', '6*27', '6*91', '9*80',
            '35*15', '3*8*7', '5*95', '56*53', '357*87']
ft = ""
tugri_javoblar = 0
while True:
    a = input('\033[1;32m Математика\033[1;33m тест \n\033[1;36m        Напишите start или quit \n')
    if a.lower() == 'start':
        print('\033[1;32m  Начинаем')
        i = 0
        for x in javoblar:
            answer = input(f'\033[0;0m {i+1}: {savollar[i]}\n')
            if answer == javoblar[x]:
                print('\033[1;32m  Правильно\033[0;0m')
                tugri_javoblar += 1
            else:
                print('\033[1;31m Ошибка')
            i +=1
        if tugri_javoblar == 0:
            print('\033[1;31m Ты дебил?')
            break
        elif tugri_javoblar == 10:
            ft = input(f'\033[1;32m     Молодец ты смог решить все задачи! Press F to Win\n')
        elif tugri_javoblar <=5:
            ft = input(f'\033[1;33m Ты ответил правильно на {tugri_javoblar} вопросов! Press F to finish\n')
        else:
            ft = input(f'\033[1;32m Ты ответил правильно на {tugri_javoblar} вопросов! Press F to finish\n')
        if ft.lower() == 'f':
            print('\033[3;33;3m       Created By Shoimov Sarvar\033[0;0m')
            break
        else:
            print('\033[1;31m Ты дебил?')
            break
    elif a.lower() == 'quit':
        break
    else:
        print('\033[1;31m Ошибка')
