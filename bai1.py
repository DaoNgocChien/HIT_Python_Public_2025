<<<<<<< HEAD
print("khkhhk")
=======
n = int(input("Nhập năm : "))
t = int(input("Nhập tháng : "))
nam_nhuan = False 
if n % 4 == 0 :
    nam_nhuan = True 
if t in [1 ,3 , 5 , 7 , 8 , 10 , 12] : 
    so_ngay = 31 
if t in [ 4 , 6 , 9 , 11 ] : 
    so_ngay = 30
elif t == 2 :
    if nam_nhuan : 
        so_ngay = 29 
    else :  so_ngay = 28 

print(f"tháng {t} năm {n} có {so_ngay} ngày")
 

>>>>>>> f5cb036 (BTVN2)
