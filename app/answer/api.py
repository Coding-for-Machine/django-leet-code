import ast
import subprocess
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Schema
from problems.models import Function, Problem, Language, AlgorithmTest, TestCase
from .models import Solution

api = NinjaAPI()

class SolutionSchema(Schema):
    problem_id: int
    language_id: int
    code: str

def is_safe_function(code: str) -> bool:
    """Kod xavfsizligini AST orqali tekshirish"""
    dangerous_functions = {
        "os", "eval", "exec", "subprocess", "open", 
        "shutil", "socket", "pickle", "ctypes", 
        "ftplib", "pdb", "base64", "xmlrpc", "paramiko"
    }
    
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in dangerous_functions:
                    return False
    except Exception:
        return False
    
    return True

def extract_function_info(code: str):
    """Koddan funksiya nomi va argumentlarini olish"""
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
                args = [arg.arg for arg in node.args.args]
                return func_name, args
    except Exception as e:
        print(f"Xatolik: {e}")
    return None, []

def file_code_write(user_code: str):
    """Foydalanuvchi kodini faylga xavfsiz yozish"""
    if not is_safe_function(user_code):
        return None, "Xavfli kod aniqlandi!"
    
    func_name, func_args = extract_function_info(user_code)
    if not func_name:
        return None, "Xato: Funksiya topilmadi yoki sintaksis xato!"
    
    func_args_str = ", ".join(func_args)
    wrapper_code = f"""
def convert_input(data):
    print(data)
    try:
        return int(data)  # Agar butun son bo‘lsa
    except ValueError:
        try:
            return float(data)  # Agar o‘nlik kasr bo‘lsa
        except ValueError:
            try:
                return eval(data)  # Agar list, tuple, dict bo‘lsa
            except:
                return data.strip('"').strip("'")  # Agar string bo‘lsa

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read()
    converted_args = list(map(convert_input, input_data))  # Barcha argumentlarni aylantirish
    print({func_name}(*converted_args))
"""
    
    file_path = "user_code.py"
    with open(file_path, "w") as temp_file:
        temp_file.write(user_code + "\n" + wrapper_code)
    
    return file_path, None

def run_python_code(file_path: str, test_cases):
    """Kod faylini test caselar bilan ishlatish"""
    passed_tests = 0
    total_tests = len(test_cases)
    execution_time = 0.1  # Soxta vaqt natijasi
    memory_usage = 1.5  # Soxta xotira natijasi
    
    for test in test_cases:
        try:
            process = subprocess.run(
                ["python3", file_path],
                input=test.input_data,
                capture_output=True,
                text=True,
                timeout=5
            )
            if process.stdout.strip() == test.output_data.strip():
                passed_tests += 1
        except subprocess.TimeoutExpired:
            return 0, total_tests, execution_time, memory_usage, "Timeout error"
        except Exception as e:
            return 0, total_tests, execution_time, memory_usage, str(e)
    
    return passed_tests, total_tests, execution_time, memory_usage, None

@api.post("/submit/")
def submit_solution(request, data: SolutionSchema):
    user = request.user
    problem = get_object_or_404(Problem, id=data.problem_id)
    language = get_object_or_404(Language, id=data.language_id)
    
    if language.name.lower() != "python":
        return {"error": "Only Python code execution is supported"}
    
    algorithm = AlgorithmTest.objects.filter(problem=problem, language=language).first()
    if not algorithm:
        return {"error": "Algorithm test not found for this problem and language"}
    
    test_cases = TestCase.objects.filter(algorithm=algorithm)
    file_path, error = file_code_write(data.code)
    if error:
        return {"error": error}
    
    passed_tests, total_tests, execution_time, memory_usage, run_error = run_python_code(file_path, test_cases)
    if run_error:
        return {"error": run_error}
    
    solution = Solution.log_solution(
        user=user,
        problem=problem,
        language=language,
        code=data.code,
        execution_time=execution_time,
        memory_usage=memory_usage,
        passed_tests=passed_tests,
        total_tests=total_tests
    )
    
    return {"solution_id": solution.id, "is_accepted": solution.is_accepted, "score": solution.score}
