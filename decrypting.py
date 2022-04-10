import pyAesCrypt
import os


# функция дешифровки
def decryption(file, password):
    # задаем размер буфера
    buffer_size = 512 * 1024

    # вызываем метод дешифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # что бы видеть результат программы
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' дешифрован]")

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
                decryption(path, password)
            except Exception as ex:
                print(ex)

        # если находим директорию , то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)

def main():
    password = input("Введите пароль для дешифрования: ")
    walking_by_dirs("c:\\t", password)

if __name__ == "__main__":
    main()

