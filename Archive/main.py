import zipfile
import os
d = input('Выберете действие (A - архивация, U - разархивация): ')
if d == 'A':
    archive = zipfile.ZipFile('/Users/tretyakov/FolderTest/trash.zip', 'w')
    for root, dirs, files in os.walk('/Users/tretyakov/FolderTest/'):
        for file in files:
            archive.write(os.path.join(root, file))
    archive.close()
    print('Архивация успешно завершена!')
elif d == 'U':
    archive = zipfile.ZipFile('/Users/tretyakov/FolderTest/trash.zip')
    archive.extractall('/Users/tretyakov/FolderTest/')
    archive.close()
    print('Файл успешно разархивирован!')
else:
    print('Ошибка, неопознанная комманда!')