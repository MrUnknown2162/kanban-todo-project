# Hàm đơn giản không có tham số
def greet():
    print("Hello, World!")

# Hàm có tham số
def greet_person(name):
    print(f"Hello, {name}!")

print("=== Testing functions ===")
greet()
greet_person("Alice")

# Hàm có giá trị trả về
def add_numbers(a, b):
    result = a + b
    return result

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Hàm tính điểm trung bình
def calculate_average(scores):
    # push your code here
    pass

scores = [85, 90, 78, 92, 88]
avg = calculate_average(scores)
print(f"Average score: {avg:.2f}")
   
# Hàm kiểm tra số chẵn lẻ
def check_even_odd(number):
    # push your code here
    pass

print(f"7 is {check_even_odd(7)}")
print(f"8 is {check_even_odd(8)}")

# Hàm quản lý thông tin sinh viên
def create_student(name, age, major):
    student = {
        "name": name,
        "age": age,
        "major": major,
        "courses": []
    }
    return student

def add_course(student, course):
    # push your code here
    pass

# Tạo và quản lý thông tin sinh viên
student1 = create_student("John Doe", 21, "Computer Science")
print("Student created:", student1)

add_course(student1, "Python Programming")
add_course(student1, "Data Structures")
print("Final student info:", student1)








