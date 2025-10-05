# Xử lý lỗi chia cho 0
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Please provide numbers only!")
        return None

# Xử lý lỗi truy cập list
def safe_get_item(my_list, index):
    try:
        item = my_list[index]
        return item
    except IndexError:
        print(f"Error: Index {index} is out of range!")
        return None
    except TypeError:
        print("Error: Index must be a number!")
        return None

# Xử lý lỗi chuyển đổi kiểu dữ liệu
def safe_convert_to_int(value):
    try:
        result = int(value)
        return result
    except ValueError:
        print(f"Error: '{value}' cannot be converted to integer!")
        return None

# Xử lý lỗi khi đọc file
def safe_read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'!")
        return None
    finally:
        print("File operation completed (success or error)")

# Test exception handling
print("=== Testing Exception Handling ===")

# Test safe divide
print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))
print("10 / 'a' =", safe_divide(10, 'a'))

# Test safe get item
my_list = [1, 2, 3, 4, 5]
print("Item at index 2:", safe_get_item(my_list, 2))
print("Item at index 10:", safe_get_item(my_list, 10))

# Test safe convert
print("Convert '123':", safe_convert_to_int('123'))
print("Convert 'abc':", safe_convert_to_int('abc'))

# Test safe read file
content = safe_read_file('nonexistent.txt')
