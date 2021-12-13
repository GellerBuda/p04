# Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!

szám = int(input('Adj meg egy egész számot! ' ))
szám1 = int(input('Adj meg egy másik egész számot! '))
szám2 = int(input('Adj meg egy harmadik egész számot! '))


if szám1 > szám < szám2:
  print(szám, 'a kissebb!')

if szám > szám1 < szám2:
  print(szám1, 'a kissebb!')

if szám1 > szám2 < szám:
  print(szám2,'a kissebb!')
