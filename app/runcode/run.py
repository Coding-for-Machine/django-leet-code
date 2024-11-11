
import subprocess
from subprocess import Popen
from .models import Problems, Language
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils.html import format_html
import os
from django.http import JsonResponse

# rest 
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# my moduls get test 

# for i in test:
#     print(i.test_name)

def file_open(request, file_name, input_code):
    if str(request.user.email) not in os.listdir():
        os.mkdir(f"{str(request.user.email)}")
    else:
        with  open(f"{str(request.user.email)}/{file_name}", mode="w") as f:
            f.write(input_code)
            f.close()
    return f
 
context_list = []

# @api_view(['GET', 'POST'])
def run_code(request, problem_id, *args, **kwargs):
    
    code = request.POST.get('code')
    language = request.POST.get('language')
    problem = get_object_or_404(Problems, id=problem_id)
    print(problem)
    
    context_list = []
    if Language.objects.filter(name__contains='python').exists():
        for i in problem.unittestproblem_set.all():
            print(problem.unittestproblem_set.all())
            print(i.language)
            print(language)
            if str(i.language).lower()=='python'and str(i.language).lower()==language:
                input_code=i.input_code
                file_open(request,'test.py', code)
                file_open(request, "solution.py", input_code)
                run_file = f"{str(request.user.email)}/solution.py"
                out = Popen(["python3", "-m", "unittest", "-q", run_file], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
                stdout, stderr = out.communicate()
                data = str(stdout).split("======================================================================")
                list1=[{'input':{str(input_code).replace("\r", "<br>").replace("\n", "&#9").replace("\'input\'", "<dd></dd>")}}, {"error": {stderr}}, {"stdout": "<br />".join(str(data).split("\\n"))}]
               
                return HttpResponse(list1)
               
    else:
        return HttpResponse("===Bu Boshqa Dasturlash Tili==!!!")

    # return  list1


# print(context_list)












# def palindrome(string):
# 	new_str = ""
# 	for i in string:
# 		if i.isalnum():
# 			new_str += (i)
# 	return new_str.lower()[::-1] == new_str.lower()
#     """
#     os.mkdir(f'solution_file/{id}')
#     solution = open(f"solution_file/{id}/solution.py", mode="w")
#     solution.write(code)
#     solution.close()
#     # unittet
#     unit_test = open(f"test_file/{id}/test.py", mode="w")
#     for i in test:
#         i.test_body
#     unit_test.write(str(i.test_body))
#     unit_test.close()
#     run_file = f'test_file/{id}/test.py'
#     out = Popen(["python3", "-m", "unittest", "-q", run_file], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
#     stdout, stderr = out.communicate()
#     data = str(stdout).split("======================================================================")
#     # for i in test:
#     #     return  i.test_body
#     response = {
#         "error": {stderr}, # test_# : error message / passed,
#         "input": {i for i in test if i.test_body},
#         "stdout": "<br />".join(str(stdout).split("\\n"))
#     }
#     print(response)


    # for i in range(1, len(data)):
    #     info = ("<br />".join(data[i].split("\\n")).split("----------------------------------------------------------------------")[1])
    #     number = int(info.split("test_")[1][0])
    #     response["error"][number] = info
    # for i in range(1, 8):
    #     try:
    #         response["error"][i]
    #     except KeyError:
    #         response["error"][i] = "passed"

    # update = False
    # if b"Error" in stdout:
    #     for i in range(1, 8):
    #         if response["error"][i] == "passed":
    #             response["error"][i] = "Possible Syntax-related Errors, recommend to see raw output for more information"

    # passed = True
    # for i in response["error"]:
    #     if response["error"][i] != "passed":
    #         passed = False

    # if passed:
    #     try:
    #         exist = Passed.objects.get(user_id=request.user.id, problem_id=problem)
    #     except:
    #         passed = Passed(user_id=request.user.id, problem_id=problem)
    #         passed.save()



if __name__ in '__main__':
    run_code()