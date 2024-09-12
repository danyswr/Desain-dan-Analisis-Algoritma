def perbandingan(nilai1,nilai2):
    if nilai1 > nilai2:
        return f"angka pertama lebih besar dari angka kedua = {nilai1}"
    else:
        return f"angka kedua lebih besar dari angka pertama = {nilai2}"


nilai1 = int(input("masukan angka pertama = "))
nilai2 = int(input("masukan angka keuda  = "))

hasil = perbandingan(nilai1,nilai2)
print(hasil)