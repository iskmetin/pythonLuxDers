mesafe=float(input("toplam mesafeyi giriniz:"))
litre=float(input("100kmde kac litre yakiyor:"))
litreFiyati=float(input("benzinin litresi kac lira:"))

toplamFiyat=mesafe/100*litre*litreFiyati
print("Toplamda ",toplamFiyat," lira harcadiniz")