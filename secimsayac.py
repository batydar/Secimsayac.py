from datetime import *
import time


a=0
while a==0:
    a=int(input("Sayacın açık kalacağı süreyi seçiniz: \n"))


while a>0:
    an=datetime.now()
    ay=6
    yıl=2023
    gün=18
    saat=8
    dakika=00
    saniye=00
    bugün= an.day
    buyıl= an.year
    buay= an.month
    busaat= an.hour
    budakika= an.minute
    kalansaniye=60-an.second




    if budakika>dakika:
        kalandakika=dakika+60-budakika
        saat=saat-1
    else:
        kalandakika=dakika-budakika

    if busaat>saat:
        kalansaat=saat+24-busaat
        gün=gün-1
    else:
        kalansaat=saat-busaat

    if bugün>gün:
        kalangün=gün+30-bugün
        ay=ay-1
    else:
        kalangün=gün-bugün

    if buay>ay:
        kalanay=ay+12-buay
        yıl=yıl-1
    else:
        kalanay=ay-buay

    kalanyıl=yıl-buyıl

    print("cumhurbaşkanlığı seçimine "+str(kalanyıl)+" yıl "+str(kalanay)+" ay "+str(kalangün)+" gün "+ str(kalansaat)+" saat "+ str(kalandakika)+" dakika "+str(kalansaniye)+" saniye kaldı.")
    a=a-1
    time.sleep(1)
