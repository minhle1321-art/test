import random
thuong = "abcdefghijklmnopqrstuvwxyz"
HOA = "ABCDEFGHIJKLMNOPORSTUVWXYZ"
so = "0123456789"
dac_biet = "!@#$8^&*"
tat_ca = thuong + HOA + so + dac_biet

do_dai = int(input("Độ dài: "))

if do_dai < 8: # if dieukien : (<, >, =, !, >=, <=, ==)
    print("Cần ít nhất 8 ký tự!")
else: 
    print("Độ dài hợp lệ, bắt đầu tạo mật khẩu...")
    mk = [random. choice(thuong), random. choice(HOA) ,
        random. choice(so), random. choice(dac_biet)]
    
    for i in range(do_dai - 4) :
        mk.append(random. choice(tat_ca))
        
    random. shuffle(mk)
    print("".join(mk))