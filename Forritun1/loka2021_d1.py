# Skrifið forrit sem les inn jákvæðar heiltölur frá notanda.  Forritið á að lesa inn tölurnar eina í einu þar til notandi skrifar tölu sem er neikvæð.  Þá á forritið að prenta út í vaxandi röð allar sléttu tölurnar sem notandi skrifaði.  Prentið allar tölurnar í einni línu með bil á milli talna.


num = int(input("number: "))

evennum = []
while num > 0:
    if num % 2 == 0:
        evennum.append(num)

    num = int(input("number: "))

evennum.sort()
print(" ".join(str(e) for e in evennum))
