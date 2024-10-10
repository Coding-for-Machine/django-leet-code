from answer.models import Answer
from problems.models import Javoblar, Problems



def run_code(id):
    problems = Problems.objects.get(id=id)
    answer = Answer.objects.filter(problem = problems)
    javoblar = problems.javoblar_set.all()
    soni = javoblar.count()
    for j in javoblar:
        if set(answer) in set(j.javob):
            return 

