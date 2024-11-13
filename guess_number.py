# -*- coding: utf-8 -*-
def guess_number():
    secret_number = 9
    guess = 0
    guess_limit = 3
    
    while guess < guess_limit:
        user = int(input("masukan angka > "))
        if user == secret_number:
            print("selamat, anda berhasil menebak")
            break
        else:
            print("salah!")
            guess += 1
    else:
        print(f"gagal, angkanya adalah {secret_number}")