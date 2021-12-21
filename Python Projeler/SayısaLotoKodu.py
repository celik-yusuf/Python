"""
Basit bir sayisal loto programi
metota tahmin edilen 6 adet sayi gonderir, metot ta 6 adet sayi tutar ve kac tahminin uyustugunu geri donderir.

"""

import random 

def bul(tahminler): 
    #Bilgisayarin tuttugu sayilar
    tutulanlar=[random.randint(1,50) for i in range(10)]#max 10 tane sayi dönderir
    print ("tutulanlar:",tutulanlar)
    tahmin=0
    tutan_tahminler=[] # tutan tahminleri bos bir listeye atama  islemi yapılır
    for i in tahminler:
        if tutulanlar.count(i)>0: #Tutulanlar icinde tahmin icindeki sayi varmi?
            tahmin+=1
            tutan_tahminler.append(i)
    return "tutan tahmin sayisi=",tahmin,"tutan tahminler=",tutan_tahminler #  tutan tahmin sayisi ve tutan tahminleri geri donderir.

    

tahminler=(33,13,23,44,21,49,17,41,34,40) #Tahminlerim
print ("tahminler=",tahminler)

print (bul(tahminler))
