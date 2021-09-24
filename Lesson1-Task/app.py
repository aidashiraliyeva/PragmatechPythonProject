# 1 Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.

a=int(input("1 ci eded daxil edin :"))
b=int(input("2 ci ededi daxil edin :"))
c=int(input(" 3 cü ededi daxil edin :"))
d=int(input(" 4 cü ededi daxil edin :"))

if a==b==c==d:
    print(a*a)
else:
    print(a+b+c+d)

# 2 Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.

lis = []
reqem = int(input("Arrayin olcusu:"))
print("Ededleri daxil edin:")
for i in range(reqem):
    reqemler=int(input())
    lis.append(reqemler)
    print("En boyuk eded budur:", max(lis))

# 3 Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.

meyveler={
    "banan":"3azn",
    "heyva" :"5azn",
    "nar" :"2azn"
}
meyve=meyveler

print(meyveler)

meyve=input()
if meyve in meyveler:
    print("var\n"+"Qiymet:"+meyveler[meyve])
else:
    print('yoxdur')

# 4 Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. Adın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.Əgər adını düzgün daxil edərsə, soyadının daxil etməsini istəyin. Soyad 5 hərfdən kiçik, 15 hərfdən uzun olmasın. Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin. Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır. Sonra email daxil etməsini tələb edin. Emailin uzunluğu 10 hərifdən qısa 22 hərfdən uzzun olmasın, tərkibində @gmail.com olsun və bu hissə daxil etdiyi emailin sonunda olsun. Ardınca parol axil etsin. Parol 6-13 simvol aralığında olmalıdır. Sonra parolu təsdiqləməyini tələb edin. Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır. Bütün bunlar düzgün daxil edilərsə, Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın detallarına baxmaq istəyib-istəməməsi soruşulsun. Əgər hə desə, aşağıdakı görüntü çapa verilsin: (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə, hər verdiyibiz şərtə uyğun error tipli mesaj verin. Məsələn doğum ilini 5 simvoldan ibarət daxil etsə, mesaj verilsin ki 4 simvol daxil edin. Yəni hər şərti müvafiq mesajlar ilə userə izah edin. ============================================= Ad: Murad Soyad: Əliyev Yaş: 22 Email: muradaliyev1996@gmail.com Parol: 123456789 ============================================= Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın.

# 5 Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.

cem = 0

lis = [4,2,7,5]
for i in range(0, len(lis)):
    cem = cem + lis[i]
print(cem)

# 6 Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin.

lis = [5,3,78,34,21,67]
lis.sort()
print("En boyuk eded budur:", lis[-1])

# 7 Listin en kicik elementini min funksiyasini istifade etmededen tapan alqoritm yazin.

lis = [5,3,78,34,21,67]
lis.sort()
print("En kicik eded budur:", lis[:1])

# 8 Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2

# 9 Write a Python program to check a list is empty or not.

lis1=[2,4,6,7,8]
lis2=[]

if lis2:
    print("Lis bos deyil")
else:
    print("Lis bosdur")

# 10 my_text = “Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.” my_text stringindeki sozler elifba sirasi ile duzub string formatinda ekrana yazdirin.

# 11 Write a Python program to select the odd items of a list.

reqemler = [1,2,3,4,5,6,7]
print(reqemler[::2])


# 12 Write a Python function to sum all the numbers in a list.

cem = 0
reqem = 0
lis = [1,2,3,4,5,6,7]
while(reqem<len(lis)):
    cem = cem+lis[reqem]
    reqem+=1
    print(cem)

#  15 Sample List : (8, 2, 3, -1, 7) Expected Output : -336

reqemler = [1,2,3,4,5,6,7]
reqem=1

for inb in reqemler:
    reqem=reqem * inb
    print(reqem)