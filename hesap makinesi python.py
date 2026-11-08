while True:
    print("Hesap Makinesi Programına Hoşgeldiniz ...")
    adet = int(input("Kaç adet sayı gireceksiniz? "))
    sayılar = []
    for i in range(adet):
        sayı=float(input(f"{i+1}.sayıyı giriniz "))
        sayılar.append(sayı)
    işlem=input("Hangi işlemi yapmak istiyorsunuz? (+,-,*,/,**,sqrt) ")
    if işlem=="+":
        toplam = 0
        for sayı in sayılar:
            toplam+=sayı
        print("Sayıların toplamı : ",toplam)
    elif işlem=="-":
        fark=sayılar[0]
        for sayı in sayılar[1::]:
            fark-=sayı
        print("Sayıların farkı : ",fark)
    elif işlem=="*":
        çarpım=1
        for sayı in sayılar:
            çarpım*=sayı
        print("Sayıların çarpımı : ",çarpım)
    elif işlem=="/":
        bölüm=sayılar[0]
        for sayı in sayılar[1::]:
            if sayı==0:
                print("Bir sayı sıfıra bölünemez.")
                break
            bölüm/=sayı
        print("Sayıların bölümü : ",bölüm)
    elif işlem=="**":
        üs=sayılar[0]
        for sayı in sayılar[1::]:
            üs**=sayı
        print("Sayıların üssü : ",üs)
    elif işlem=="sqrt":
        for sayı in sayılar:
            if sayı<0:
                print("Negatif sayının karekökü alınamaz.")
                break
            karekök=sayı**0.5
        print(sayı , "sayısının karekökü : ",sayı**0.5)
    else :
        print("Geçersiz işlem seçtiniz ... Program kapatılıyor.")

    devammı=input("Devam etmek istiyormusunuz? (EVET/HAYIR) ")
    if devammı.upper()=="HAYIR":
        print("Program kapatılıyor ... İyi günler dileriz.")
        break
    
