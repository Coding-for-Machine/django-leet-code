from django.db import models
from runcode.models import Problems, Language
import os
from pathlib import Path

DIR = Path(__file__).resolve().parent.parent

def file_create(path_dir, file_name, input_code, function_name=None):
    new_file_path = os.path.join(path_dir, f'{file_name}.py')
    try:
        with open(new_file_path, 'w') as f:
            f.write(input_code)
            print(f"{new_file_path} fayli yaratildi.")
    except Exception as e:
        print(f"Xato fayl yaratishda: {e}")


    # fileni imort qilish
    if function_name:
        try:
            with open(new_file_path, 'r') as file:
                content = file.readlines()
            func_name = f"from unittest_user import {function_name}"
            content.insert(0, func_name + '\n')

            with open(new_file_path, 'w') as file:
                file.writelines(content)
        except Exception as e:
            print(f"Xato faylni yangilashda: {e}")

def create_dirs(dir_name):
    try:
        os.makedirs(dir_name, exist_ok=True)
        print(f"{dir_name} katalogi yaratildi.")
    except Exception as e:
        print(f"Xato katalog yaratishda: {e}")

class Unittestproblems(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    language = models.OneToOneField(Language, on_delete=models.CASCADE)
    unit_test_class_name = models.CharField(help_text="pastdagi kiritgan class nomi bo'lishi kerak!!!", max_length=100)
    unit_test_code = models.TextField(help_text="misol: python dasturlash tilidagi unittest orqali yozilgan kod bo'lish kerak yoki boshqa dasturlash tilida u dasturlash tillari qo'shilgan bo'lsa!!!")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Unittestproblems, self).save(*args, **kwargs)
        try:
            language_name = self.language.name.strip()
            new_directory_path = os.path.join(DIR, "problemstest")
            create_dirs(new_directory_path)
            new_language_path = os.path.join(new_directory_path, language_name)
            create_dirs(new_language_path)

            file_name = f"{language_name}{self.problem.id}test{self.id}"
            file_create(new_language_path, file_name, self.unit_test_code, self.problem.function_or_class_name)
        except Exception as e:
            print(f"Xato: {e}")

    def __str__(self):
        return f"{self.language.name} {self.problem.name if self.problem else ''}"

class Memorytime(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    language = models.OneToOneField(Language, on_delete=models.CASCADE)
    memory_time_code = models.TextField(help_text="misol: python dasturlash tilidagi tracemalloc (3.4 versiadan yuqorida ishlaydi) orqali yozilgan kod bo'lish kerak yoki boshqa dasturlash tilida u dasturlash tillari qo'shilgan bo'lsa")
    line1 = models.TextField(help_text="User  uchun 1 kod(python dasturlash tilidagi tracemalloc yozilgan)")
    line2 = models.TextField(help_text="User  uchun 1 kod(python dasturlash tilidagi tracemalloc yozilgan)")

    def save(self, *args, **kwargs):
        super(Memorytime, self).save(*args, **kwargs)
        language = self.language.name
        new_path = os.path.join(DIR, "problemstest")
        create_dirs(new_path)
        language_path = os.path.join(new_path, "".join(language.strip()))
        create_dirs(language_path)

        filesxotir = str(self.language.name)+ str(self.problem.id) + "time" + str(self.id)
        file_create(language_path, filesxotir, self.memory_time_code)

        # line 1
        fileline1 = str(self.language.name)+ str(self.problem.id)+ "time" + str(self.id) + "line1"
        file_create(language_path, fileline1, self.line1)

        # line 2
        fileline2 = str(self.language.name) + str(self.problem.id) + "time" + str(self.id) + "line2"
        file_create(language_path, fileline2, self.line2)


    def __str__(self):
        return str(self.language.name + (self.problem.name if self.problem else ""))
