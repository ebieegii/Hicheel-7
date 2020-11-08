#2 too ogogdson bol hoorondoh tegsh toonuudin niilber ol

a = int(input('a: '))
b = int(input('b: '))

ma = max(a,b)
mi = min(a,b)
niilber = 0
while mi <= ma:
    if mi % 2 == 0:
        niilber += mi
    mi += 1
print("niilber: ",niilber)