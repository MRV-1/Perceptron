#AND MODEL
x1 = [0,0,1,1]
x2 = [0,1,0,1]
waitedOutput =  [0,0,0,1]
w1 = [1.2,1.3,1.4,0.5]
w2 = [1.2,1.3,1.4,0.5]
threshold = 1.5 # AND problemi için sigmoid esik degeri
bias = 0.1
fNET = 0


def weighted_sum(i):
    fNET = x1[i]*w1[i]+x2[i]*w2[i];
    return fNET


def activation_func(fNET):
    if fNET>threshold:  #fnet değeri threshold'dan büyükse 1 çıktısını versin, değilse 0 çıktısını versin
       output=1
    else:
       output=0
    return output


def agirliklari_yeniden_hesapla(Ç,i):           #hatalı durumda ağırlıkların yeniden hesaplanması
    print(" waited output : ", waitedOutput[i])
    if( Ç != waitedOutput[i] ):
        if Ç > waitedOutput[i]:
            #w1 için x1 kullanılıyor
            w1[i] = w1[i] - bias * x1[i]
            print("w1[i] :", w1[i])
            #w2 için x2 kullanılıyor
            w2[i] = w2[i] - bias * x2[i]
            print("w1[i] :", w1[i])
            print("if'teyim")
        else :
             #w1 için x1 kullanılıyor
            w1[i] = w1[i] + bias * x1[i]
            print("w1[i] :", w1[i])
            #w2 için x2 kullanılıyor
            w2[i] = w2[i] + bias * x2[i]
            print("w2[i] :", w2[i])
            print("elif'deyim")
    print("ağırlık güncelleme fonk. dönen deger w1 :",w1[i])
    print("ağırlık güncelleme fonk. dönen deger w2 :",w2[i])


#Ç =[0,0,0,0];
i=0
for i in range(3):
    print("i : ",i)#1 yazdığımda ilk 4 girişin hepsi 1 kere çalışacak
    for j in range(len(waitedOutput)):
        print("j = ",j);
        a = weighted_sum(j);                         #x1 ve x2'nin sırasıyla netleri hesaplanacak
        print("ağırlık : ",a)
        Ç = activation_func(a)                      #step_func=activation_func çıktısını görmek
        print("ç: ", Ç)
        agirliklari_yeniden_hesapla(Ç,j)            #ve ağırlıkları yeniden hesaplamak
        print(" Ç :",Ç)
print("Eğitim tamamlandı!\n Eğitim sonrası ağırlıklar: w1 ")
print(w1)
print("Eğitim tamamlandı!\n Eğitim sonrası ağırlıklar: w2 ")
print(w2)
