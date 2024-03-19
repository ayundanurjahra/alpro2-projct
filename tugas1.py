##  Program Python Menghitung Faktorial  ##
  
angka = int(input('Input angka: '))
 
hasil = 1
for i in range(1,angka+1):
  hasil = hasil * i
 
print(angka,'!=',hasil,sep='')


##  Program Python konversi suhu ##

celcius= float(input('input suhu celsius'))

fahrenheit = (9/5 * celcius) + 32
kelvin = celcius * 273
reamur = celcius * (4/5)

print(celcius,'derajat Celsius =',fahrenheit,'derajat Fahrenheit')
print(celcius,'derajat Celsius =',kelvin,'derajat Kelvin')
print(celcius,'derajat Celsius =',reamur,'derajat Reamur')