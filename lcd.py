def find_lcd(a, b):
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1

a = 12
b = 18
print("LCD:", find_lcd(a, b))
