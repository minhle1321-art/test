import random

# Main
thuong = "abcdefghijklmnopqrstuvwxyz" 
HOA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
so = "0123456789"
dac_biet = "!@#$%^&*"
tat_ca = thuong + HOA + so + dac_biet


do_dai = int(input("Độ dài mật khẩu: "))            # Bat buoc moi nhom co it nhat 1 ky tu

if do_dai < 8:
    print("You need atleast 8 characters!")
else:
    print("Character amount accepted, start creating your password...")

    mk = [random. choice(thuong), random. choice(HOA),
        random. choice(so), random. choice(dac_biet)]

    for _ in range(do_dai - 4):         # Them phan con lai tu tat_ca
        mk.append( random. choice(tat_ca))

    random. shuffle(mk)         # tron ngau nhien
    mat_khau = "".join(mk)      # ghep list thanh chuoi
    print("Mật khẩu:", mat_khau)

# Test

# 1
# list = [1,2,3,4,5,6] #Quotation marks also work
# print (f"Result:\nYou got: {random.choice(list)}")

# # 2
# list2 = ["Heads", "Tails"]
# print (f"Result:\nFlipped a coin: {random.choice(list2)}")

# # 3
# thuong = "abcdefghijklmnopqrstuvwxyz" 
# HOA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# so = "0123456789"
# dac_biet = "!@#$%^&*"
# # (Chua xong)


# 4
# so = "0123456789"
# list3 = []
# for i in range(6): 
#     list3.append(random.choice(so))
# together = "".join(list3)
# print (together) #Take 6 random numbers from the list

#5


#Notes

"""
random.randint = random integer


"""
