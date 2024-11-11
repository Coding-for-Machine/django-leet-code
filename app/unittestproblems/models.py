from django.db import models 
from runcode.models import Problems, Language
import os
from pathlib import Path

DIR = Path(__file__).resolve().parent.parent

def file_create(path_dir, file_name, input_code):
    new_file_path = os.path.join(path_dir, f'{file_name}.py')
    try:
        with open(new_file_path, 'w') as f:
            f.write(input_code)
            print(f"{new_file_path} fayli yaratildi.")
    except Exception as e:
        print(f"Xato: {e}")

def create_dirs(dir_name):
    try:
        os.makedirs(dir_name, exist_ok=True)
        print(f"{dir_name} katalogi yaratildi.")
    except Exception as e:
        print(f"Xato: {e}")
    return dir_name
class Unittestproblems(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    language = models.OneToOneField(Language, on_delete=models.CASCADE)
    unit_test_code = models.TextField(help_text="misol: python dasturlash tilidagi unittest orqali yozilgan kod bo'lish kerak yoki boshqa dasturlash tilida u dasturlash tillari qo'shilgan bo'lsa!!!")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            super(Unittestproblems, self).save(*args, **kwargs)  # Modelni saqlash
            language = self.language.name
            new_directory_path = os.path.join(DIR, "problemstest")
            create_dirs(new_directory_path)
            new_language_path = os.path.join(new_directory_path, "".join(language.strip()))
            create_dirs(new_language_path)

            files = str(self.language.name) + "test" + str(self.id)  # Fayl nomi
            file_create(new_language_path, files, self.unit_test_code)  # Fayl yaratish
        except Exception as e:
            print(f"Xato: {e}")

    def __str__(self):
        return str(self.language.name + (self.problem.name if self.problem else ""))

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

        filesxotir = str(self.language.name) + "time" + str(self.id)
        file_create(language_path, filesxotir, self.memory_time_code)

        # line 1
        fileline1 = str(self.language.name) + str(self.id) + "line1"
        file_create(language_path, fileline1, self.line1)

        # line 2
        fileline2 = str(self.language.name) + str(self.id) + "line2"
        file_create(language_path, fileline2, self.line2)


    def __str__(self):
        return str(self.language.name + (self.problem.name if self.problem else ""))

# Yangi katalogning to'liq yo'lini aniqlash

# def project_starter(project_name):
#     path = Path.cwd().absolute()/"problem_test"/project_name
#     path.mkdir()
#     (path/"unittest.py").touch()
#     (path/"timetest.py").touch()
    
# if __name__ == "__main__":
#     parser = ArgumentParser()
#     parser.add_argument("project_name", help="Loyihaning nomi")
#     args = parser.parse_args()
#     project_starter(args.project_name)