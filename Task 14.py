import os
result = os.popen('dir').read()
print("Список файлов и папок в текущем каталоге:")
print(result)