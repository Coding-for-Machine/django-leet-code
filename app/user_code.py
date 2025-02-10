def add(x, y):
    return x+y

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
    input_data = sys.stdin.readlines()
    converted_args = list(map(convert_input, input_data))  # Barcha argumentlarni aylantirish
    print(converted_args)
    print(add(*converted_args))
