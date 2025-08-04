<<<<<<< HEAD
n = int(input("Nhập số nguyên : "))
dem = 0 
tong = 0 
so = abs(n) 
while so > 0 :
    chu_so = so % 10 
    tong += chu_so 
    dem +=1 
    so //= 10
print(n, " có ", dem, " chữ số tổng các chữ số là: ", tong) 
=======
#Nhập các phần tử n và m 
n = int(input(("Nhập số phần tử của mảng (n) : ")))
m = int(input(("Nhập số phần tử của mỗi tập A và B : ")))
#Nhập mảng 
arr = [] 
for i in range(n) :
    x = int(input(f"Nhập phần tử thứ {i+1} : "))
    arr.append(x)
#Nhập tập A 
A = set() 
print(f"Nhập {m} phần tử mà bạn thích : ")
for i in range(m) : 
    x = int(input(f"Nhập phần tử A{i+1} :"))
    A.add(x) # remove : xóa phần tử set
#Nhập tập B
B = set()
print(f"Nhập {m} phần tử bạn ghét :")
for i in range(m) :
    x = int(input(f"Nhập phần tử B{i+1} : "))
    B.add(x) # remove : là xóa pt set()
happy = 0 
for x in arr :
    if x in A : 
        happy += 1 
    elif x in B : 
        happy -= 1
print("Số điểm hạnh phúc" , happy)
>>>>>>> 6832335 (upbtvnbuoi3)
