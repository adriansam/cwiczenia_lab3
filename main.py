#skladnia z urzyciem pętli
# lista=[]
# for element in zakres:
#     if warunek_na(element):
#         lista.append("Cos sie dzieje z"element)
#
# lista=["Cos sie dzieje z " element for element in zakres if warunek_na(element)]

# lista_a=[]
# for i in range(10):
#     lista_a.append(i**2)
# print(lista_a)
#
# a=[i**2 for i in range(10)]
# print(a)
#
# lista_b = []
# for j in range(6):
#     lista_b.append(3**j)
# print(lista_b)
#
# b=[3**j for j in range(6)]
# print(b)
#
# lista_c=[]
# for k in lista_a:
#     if k%2==1:
#         lista_c.append(k)
# print(lista_c)
#
# c=[x for x in a if x%2==1]
# print(c)
#
# liczby=[1,2,3,4,5,6,7,8,9,10]
# listy=[]
# for a in liczby:
#     if a % 2 == 0:
#         listy.append(a)
# print(listy)
#
# lista2=[x for x in liczby if x % 2 == 0]
# print(lista2)

# lista=[]
# for i in [1,2,3]:
#     for j in [4,5,6]:
#         lista.append((i,j))
# print(lista)
#
# lista2=[(i, j) for i in [1,2,3] for j in [4,5,6]]
# print(lista2)

# slownik = {"PZU": "Panstwowy zaklad ubezpieczen",
#            "ZUS": "Zaklad ubezpieczen spolecznych",
#            "PKO": "Panstwowa kasa oszczednosci"}
# print(slownik)
# slownik2 = {}
# for key,value in slownik.items():
#     slownik2[value] = key
# print(slownik2)
#
# odwrocone = {value: key for key, value in slownik.items()}
# print(odwrocone)

# import math
# def funkcja_kwadratowa(a, b, c):
#     delta = b**2 - 4 * a * c
#     if delta < 0:
#         print("brak pierwiastkow")
#         return -1
#     elif delta == 0:
#         print("jeden pierwiastek")
#         x = (-b)/(2*a)
#         return x
#     else:
#         print("dwa pierwiastki")
#         x1 = (-b - math.sqrt(delta)/(2*a))
#         x2 = (-b + math.sqrt(delta)/(2*a))
#         return x1,x2
#
# print(funkcja_kwadratowa(6,1,3))
# print(funkcja_kwadratowa(1,2,1))
# print(funkcja_kwadratowa(1,4,1))

# def dlugosc_odcinka(x1=0, y1=0, x2=0, y2=0):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)
#
# #wartosci domyslne
# print(dlugosc_odcinka())
# #wlasne wartosci, argumenty pozycyjne
# print(dlugosc_odcinka(1,2,3,4))
# #mieszane wartosci
# print(dlugosc_odcinka(2,2,y2=2,x2=1))
# #wartosci nie w kolejnosci
# print(dlugosc_odcinka(y2=5,x1=2,y1=2,x2=6))
# #dwie pierwsze wartosci domyslne, dwie podajemy sami
# print(dlugosc_odcinka(x2=2,y2=2))

# def ciag(* liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         suma = 0
#         for i in liczby:
#             suma += i
#         return suma

# print(ciag())
# print(ciag(1, 2, 3.5, 4, 5, 6, 7))

# def to_lubie(** rzeczy):
#     for cos in rzeczy:
#         print("To jest")
#         print(cos)
#         print("co lubie")
#         print(rzeczy[cos])
#
# to_lubie(slodycze='czekolada', rozrywka=['gry','filmy'])

# from teksty import *
#
# a='Ala ma kota'
#
# litery.wyswietl(a)
# print(litery.dlugosc(a))
