
import subprocess
from subprocess import Popen
from .models import Problems, Language
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import os
from pathlib import Path


# yo'nalish projectim izgacha 
DIR = Path(__file__).resolve().parent.parent

# file create 
def file_create(input_code, line1=None, line2=None, *args, **kwargs):
    file_path = "problemstest/python/unittest_user.py"
    line1 = f"problemstest/python/{line1}.py"
    line2 = f"problemstest/python/{line2}.py"
    try:
        # Birinchi faylni o'qish
        with open(line2, 'r') as f1:
            first_content = f1.read()  # Birinchi fayl mazmunini o'qish

        # Uchinchi faylni o'qish
        with open(line1, 'r') as f3:
            third_content = f3.read()  # Uchinchi fayl mazmunini o'qish

        # Ikkinchi faylga yozish
        with open(file_path, 'w') as f2:
            f2.write(third_content + '\n')  # Uchinchi fayl mazmunini yozish
            f2.write(input_code + '\n')
            f2.write(first_content)  # Birinchi fayl mazmunini yozish

        print(f"'{line1}' va '{line2}' fayllari '{file_path}' fayliga muvaffaqiyatli qo'shildi.")
    except Exception as e:
        print(f"Xato: {e}")

# katalok yaratadi 
def create_dirs(dir_name):
    try:
        os.makedirs(dir_name, exist_ok=True)
        print(f"{dir_name} katalogi yaratildi.")
    except Exception as e:
        print(f"Xato cerate dirs: {e}")
    return dir_name

# kodni ishga tushitish 
def run_code(request, problem_id, *args, **kwargs):
    code = request.POST.get('code')
    language = request.POST.get('language')
    problem = get_object_or_404(Problems, id=problem_id)
    if "python"==str(language).lower():
        # for i in problem.unittestproblem_set.all():
        #     print(problem.unittestproblem_set.all())
        #     if str(i.language).lower()=='python'and str(i.language).lower()==language:
        #         input_code=i.input_code
        #         file_open(request,'test.py', code)
        #         file_open(request, "solution.py", input_code)
        #         run_file = f"{str(request.user.email)}/solution.py"
        #         out = Popen(["python3", "-m", "unittest", "-q", run_file], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
        #         stdout, stderr = out.communicate()
        #         data = str(stdout).split("======================================================================")
        #         list1=[{'input':{str(input_code).replace("\r", "<br>").replace("\n", "&#9").replace("\'input\'", "<dd></dd>")}}, {"error": {stderr}}, {"stdout": "<br />".join(str(data).split("\\n"))}]
        #         return HttpResponse(list1)

        # unittest
        try:
            # Katalok yaratadi
            new_directory_path = os.path.join(DIR, "problemstest")
            create_dirs(new_directory_path)
            # language uchun katalok yaratadi
            new_language_path = os.path.join(new_directory_path, "".join(language.strip()))
            create_dirs(new_language_path)
            # line1 
            line1 = str(language) + str(problem_id) + "time" + str(problem.memorytime_set.all().order_by("-id")[0].id) + "line1"
            # line 2
            line2 = str(language) + str(problem_id) + "time" + str(problem.memorytime_set.all().order_by("-id")[0].id) + "line2"
            file_create(code, line1, line2)  # Fayl yaratish user uchun 
            # unittest faylini yaratish
            unittest_problems = problem.unittestproblems_set.all().order_by("-id")[0]
            print("===========================================------------------================",unittest_problems)
            unittest_file = "python" + str(problem_id) + "test" + str(unittest_problems)  # Fayl nomi

        except Exception as e:
            print(f"Xato: {e}")

        file_unittest = f"problemstest/python/{unittest_file}.py"
        print(file_unittest)
        out = Popen(["python3", "-m", "unittest", "-q", file_unittest], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        data = str(stdout).split("======================================================================")
        list1=[{'input':{str(code).replace("\r", "<br>").replace("\n", "&#9").replace("\'input\'", "<dd></dd>")}}, {"error": {stderr}}, {"stdout": "<br />".join(str(data).split("\\n"))}]

        return HttpResponse(list1)
    else:
        return HttpResponse("===Bu Boshqa Dasturlash Tili==!!!")
    