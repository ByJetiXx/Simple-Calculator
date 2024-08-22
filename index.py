def hesap_makinesi():
    islem = input ("İşlem seçin (Toplama, Çıkarma, Çaprma, Bölme): ")
    sayi1 = float(input("Birinci sayı: "))
    sayi2 = float(input("İkinci sayı: "))

    if islem == "Toplama":
        print(f"Sonuç: {sayi1+sayi2}")
    elif islem == "Çıkarma":
        print(f"Sonuç: {sayi1-sayi2}")
    elif islem == "Çarpma":
        print(f"Sonuç: {sayi1*sayi2}")
    elif islem == "Bölme":
        print(f"Sonuç: {sayi1/sayi2}")
    else:
        print("Geçersiz İşelm")

hesap_makinesi()