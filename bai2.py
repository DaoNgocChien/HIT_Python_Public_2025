<<<<<<< HEAD
l = int(input("Nhập lương nhân viên : "))
if l < 7e6 : 
    t = l * 0.1 
if l > 7e6 and l < 15e8 : 
    t = l * 0.2 
if l == 15e6 : 
    t = l * 0.3

luong = int(l - t)  
thue = int(t) 
print(f"thuế : {thue} ; Lương : {luong}")
=======
ds1 = input("Nhập mã sinh viên tại bàn 1 (cách nhau bởi dấu cách) : ")
A = set(map(int , ds1.strip().split()))
ds2 = input("Nhập mã sinh viên tại bàn 2 (cách nhau bởi dấu cách) : ")
B = set(map(int , ds2.strip().split()) )
#In thông tin 2 tập hợp
print("Danh sách mã sinh viên tại bàn 1 " , A)
print("Danh sách mã sinh viên tại bàn 2" , B)
#Sinh viên đăng kí tại cả hai bàn
sinh_vien_chung = A.intersection(B) #Giao 2 tập set 
if sinh_vien_chung : 
    print("Sinh viên đăng kí cả hai bàn :" , A)
else  : 
    print("Không có sinh viêm nào đăng kí cả hai bàn cả")
#Danh sách tổng hợp sinh viên đã đăng kí 
tong_hop = A.union(B) # hợp trong tập set
print("Danh sách đã đăng kí cả hai bàn :" , tong_hop)
#Sinh viên chỉ đăng kí bàn 1
chi_ban_1 = A.difference(B)
print("Sinh viên chỉ đăng kí bàn 1 :" , chi_ban_1)
>>>>>>> 6832335 (upbtvnbuoi3)
