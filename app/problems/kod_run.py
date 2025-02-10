import sys
import ast

# 🔹 Berilgan asosiy funksiya deklaratsiyasi
main_function_declaration = "def helperFunc(x):"

# 🔹 Funksiya nomini string manipulyatsiya orqali ajratish
main_function_name = main_function_declaration.split("(")[0].replace("def", "").strip()

# 🔹 Foydalanuvchi kiritgan kod
code = """
def Upper(s):
    result = ""
    for i in s:
        if "a" <= i <= "z":
            i = chr(ord(i) - 32)  # Harflarni kattalashtirish
        result += i
    return result

def helperFunc(x):
    return x * 2

def anotherHelper(y):
    return y + 10
"""

# 🔹 AST orqali kodni analiz qilish
tree = ast.parse(code)

# 🔹 Funksiya nomi va parametrlarini olish
functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

# 🔹 Asosiy va yordamchi funksiyalarni ajratish
main_function = None
helper_functions = set()

for func in functions:
    if func.name == main_function_name:
        main_function = func.name
    else:
        helper_functions.add(func.name)

# 🔹 Xavfli funksiyalarni bloklash
dangerous_functions = {
    "os", "eval", "exec", "subprocess", "open", 
    "shutil", "socket", "pickle", "ctypes", 
    "ftplib", "pdb", "base64", "xmlrpc", "paramiko"
}

# 🔹 Xavfsiz funksiya ekanligini tekshirish
def is_safe_function(func_name, code):
    for node in ast.walk(ast.parse(code)):
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Attribute) and func.attr in dangerous_functions:
                return False
    return True

# 🔹 Foydalanuvchidan kelgan inputni olish
input_data = sys.stdin.read().strip()

# 🔹 Kiritilgan qiymatni avtomatik mos formatga o‘tkazish
def convert_input(data):
    try:
        return int(data)  # Agar son bo‘lsa, integerga o‘tkazamiz
    except ValueError:
        try:
            return eval(data)  # Agar list yoki dict bo‘lsa, shunday qoldiramiz
        except:
            return data.strip('"').strip("'")  # Agar string bo‘lsa, toza formatda qaytaramiz

input_data = convert_input(input_data)

# 🔹 Funksiyani ishga tushirish
if main_function and __name__ == "__main__":
    if is_safe_function(main_function, code):
        exec(code)  # Kodni ishga tushiramiz
        func = globals().get(main_function)  # Funksiya obyektini olish
        if func:
            result = func(input_data)  # Foydalanuvchi kiritgan funksiya chaqiriladi
            print(result)
        else:
            print("Funksiya topilmadi!")
    else:
        print("🚨 Xavfsiz bo'lmagan kod kiritildi!")

# 🔹 Funksiya natijalarini chiqarish
print("📌 Asosiy funksiya:", main_function)
print("📌 Yordamchi funksiyalar:", helper_functions)
