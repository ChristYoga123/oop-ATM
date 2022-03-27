import random as rn
import datetime as dt
from customer import Customer
import os
program = Customer(1234)
trial = 0
while True:
    os.system("cls")
    user_validation = int(input("Masukkan pin anda: "))
    if user_validation != program.id:
        print("Maaf pin salah")
        trial += 1
        if trial > 3:
            print("Anda sudah melebihi batas, Ulang dari awal")
            exit()
    else:
        while True:
            user_success = input("Selamat Datang di ATM. Menu:\n1. Cek Saldo\n2. Debet\n3. Simpan\n4. Ganti Pin\n5. Keluar\n Pilih menu: ")
            if user_success == "1":
                print("Saldo anda sekarang adalah Rp", program.getBalance())
            elif user_success == "2":
                input_nominal = float((input("Masukkan nominal: ")))
                if input_nominal <= program.getBalance():
                    print("Saldo awal adalah", program.getBalance())
                    program.withdraw(input_nominal)
                    print("Withdraw sukses. Saldo anda sekarang adalah Rp", program.getBalance(), "Enter untuk kembali")
                else:
                    print("Saldo anda kurang dari nominal yang diberikan. Enter untuk kembali")
            elif user_success == "3":
                input_nominal = float((input("Masukkan nominal: ")))
                print("Saldo awal anda adalah Rp" + str(program.getBalance()))
                operation = program.deposit(input_nominal)
                print("Deposit sukses. Saldo anda sekarang adalah Rp", program.getBalance(), "Enter untuk kembali")
            elif user_success == "4":
                while True: 
                    pin_validation = int(input("Masukkan pin lama: "))
                    if pin_validation == program.id:
                        new_pin = int(input("Masukkan pin baru: "))
                        program.id = new_pin
                        print("Id anda telah dirubah")
                        break
                    else:
                        print("Pin anda salah")
            elif user_success == "5":
                print("No. Rekord: ", rn.randint(100000, 10000000))
                print("Tanggal: ", dt.datetime.now())
                print("Saldo akhir: ", program.getBalance())
                input("Terima kasih telah menggunakan program ini. Enter untuk keluar")
                exit()



            
    

