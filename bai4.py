<<<<<<< HEAD
n = int(input("Nhập số xu : "))
m = n // 28 
chai = m 
vo = m 
while vo >= 3 : 
    doi = vo // 3 
    chai += 1
    vo = vo % 3 + doi 
print("có thể mua tối đa : " , chai)
=======
#Nhập số lượng phần tử 
n = int(input("Nhập số lượng phần tử : "))
#Nhập mảng
a = []
for i in range(n) : 
    x = input(f"Nhập phần tử thứ {i+1} : ")
    a.append(x)
#Tạo tuple
b = tuple(a) 
#In tuple 
print("Tuple b : " , b )
#Đếm số phần tử dạng số
count_numeric = 0 ; 
for i in b : 
    if i.isdigit() :
        count_numeric +=1
print("Số phần tử dạng số : " , count_numeric)
>>>>>>> 6832335 (upbtvnbuoi3)
