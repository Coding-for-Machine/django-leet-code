import time
import sys


def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Massiv va qidirilayotgan qiymat
arr = [i for i in range(1000000)]  # 1 dan 1 milliongacha bo'lgan sonlar
target = 999999  # Qidirilayotgan qiymat

# Vaqtni o'lchash
start_time = time.time()
result = linear_search(arr, target)
end_time = time.time()
# Vaqtni hisoblash
elapsed_time = end_time - start_time

# Xotira sarfini ko'rsatish
memory_usage = sys.getsizeof(arr) + sys.getsizeof(target)

# Natijalarni chiqarish
print(f"Natija: {result}")
print(f"Sarflangan vaqt: {elapsed_time:.6f} soniya")
print(f"Xotira sarfi: {memory_usage} bayt")