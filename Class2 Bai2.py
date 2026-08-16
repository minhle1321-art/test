# Vairable holds = giá chỉ (value)

# """
# Biến không đặt tên trùng
# Biến không được đặt tên có kí tự đặc biệt
# Biến không không đặt tên số hoặc số ở đầu
# Biến không đặt tên có khoảng cách VD: num 1
# Biến được đặt kí tự _ VD: num_1, _num
# Biến không được đặt tên với dấu
# """


# """
# int : số nguyên VD: 1,3,7, -1, -8
# float : số thực VD: 10.7 (decimals)
# bool: True/False
# str: Kiểu chuỗi/ kí tự VD: "abc" (words)

# Toán tử sổ học:
# +
# -
# *
# /
# // VD: 10//3 = 3
# % VD: 10%3 = 1 (Remainder)
# ** VD: 2**3 = 8

# Nhập 3 môn học
# VD: Toán = 10, Văn = 8, Anh Văn : 10
# Tính điểm trung bình

# #Note
# num = input("...") #String
# num = int(input("...) #Changes input number to integer
# """

#Test
# Toan = int(input("Số điểm toán:"))
# Van = int(input("Số điểm Văn:"))
# Anh_Van = int(input("Số điểm Anh Văn:"))

# print("Điểm trung bình:",(Toan+Van+Anh_Van)/3)
"""

Nhập vào năm sinh
Tính tuổi hiện tại của bạn
Ví dụ:
Input name: Bảo
Input datetime: 2012
Output: Bảo 14 tuổi

"""

# Ten = input("Tên của bạn: ")
# Nam = int(input("Năm sinh của bạn: "))

# print(Ten,"là", 2026-Nam,"tuổi")
# print("Tên của bạn:", Ten,"\nTuổi của bạn:", 2026-Nam)

"""

Bài: Chu vi của hình chữ nhật và diện tích của chư nhật.

"""

# chieudai = int(input("Chiều dài của chữ nhật"))
# chieurong = int(input("Chiều rộng của chữ nhật"))

# print("Chu vi của chữ nhật: ", (chieudai+chieurong)*2, "\nDiện tích của chữ nhật", chieudai*chieurong)

# #New way of print
# age = 12
# print(f"Person's age:{age}")

# #f = allows vairable inside string inside the {} mark

# #Assignmenet in new way
# print(f"Chu vi của chữ nhật: {(chieudai+chieurong)*2}", f"\nDiện tích của chữ nhật:{chieudai*chieurong}")

"""
Bài: Nhấp số lượng huy chương vàng, bạc, và đồng dung f và {}
"""

# Huychuongvang = int(input("Số lượng huy chuơng vàng: "))
# Huychuongbac = int(input("Số lượng huy chuơng bạc: "))
# Huychuongdong = int(input("Số lượng huy chuơng đồng: "))

# print(f"Vàng: {Huychuongvang}", f"\nBạc: {Huychuongbac}", f"\nĐồng: {Huychuongdong}")
# print(f"Tổng: {Huychuongvang*3+Huychuongbac*2+Huychuongdong*1}")

#Version 2

# Huychuongvang = int(input("Số lượng huy chuơng vàng: "))
# Huychuongbac = int(input("Số lượng huy chuơng bạc: "))
# Huychuongdong = int(input("Số lượng huy chuơng đồng: "))

# print("Quốc Gia\tVàng\tBạc\tĐồng\tTổng điểm")
# print(f"Việt Nam\t{Huychuongvang}\t{Huychuongbac}\t{Huychuongdong}\t{Huychuongvang*3+Huychuongbac*2+Huychuongdong*1}")