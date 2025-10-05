# Khởi tạo dictionary - thông tin sinh viên
studentA = {
    "name": "Nguyen Van A",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.5,
    1:"one"
}

# In ra thông tin
print("Student info:", studentA)

# in ra tên của sinh viên
print("Name:", studentA[1])

# in ra tuổi của sinh viên
print("Name:", studentA["age"])

# Thêm thông tin phone vào sinh viên
studentA.setdefault("phone", "0123456789")
print("After adding phone:", studentA)

# push your code here
print("After adding phone:", studentA)

# Sửa thông tin gpa của sinh viên
# push your code here
studentA["gpa"] = 10
print("After updating GPA:", studentA)

# Lấy tất cả keys và values
print("Keys:", list(studentA.keys()))
print("Values:", list(studentA.values()))

# Kiểm tra key "email" có tồn tại trong dictionary không
if "email" in studentA:
    print("Email exists")
else:
    print("Email does not exist")

# Xóa thông tin
del studentA["phone"]
print("After deleting phone:", studentA)
