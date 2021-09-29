kutle=0.45359237*float(input("kilonuzu yaziniz: (pound cinsinden)"))
boy=0.0254*float(input("boyunuzu giriniz (inch cinsinden)"))

bmi=kutle/(boy*boy)
print("Vucut kutle indeksiniz: ",format(bmi,".4f"))