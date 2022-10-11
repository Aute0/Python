# Задача №1: Напишите программу, удаляющую из текста все слова содержащие "абв".

print('Эта программа удалит из вашего текста ненужные опечатки')
inc_text = str(input('Введите, что нужно удалить: '))

user_text = 'Напишите прпр абв напиабв програбвмму пропрграмму, удаляющую из \
    этого абв текстапр все вабвс слова, содерабващие содержащие "абв"'

def del_words(user_text):
    user_text = list(filter(lambda x: inc_text not in x, user_text.split()))
    return " ".join(user_text)


user_text = del_words(user_text)
print(user_text)
