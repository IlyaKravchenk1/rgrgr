import hashlib

str = input('Введите строку, состоящую только из маленьких латинских букв')

sum_sub = set()

for i in range(len(str)):
    for j in range(len(str), i, -1):
        hash_str = hashlib.sha1(str[i:j].encode('utf-8')).hexdigest()
        sum_sub.add(hash_str)

print(f'{len(sum_sub) -1} различных подстрок в строке {str}')
print(' I прошел курс, но Алгоритм Хоффмана мне не дался')
