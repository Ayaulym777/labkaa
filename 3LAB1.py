import random

def initialize_substitution_lists():
    # Инициализация алфавита и начального списка подстановки
    alphabet = list(" АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯb")
    substitution_list = list("КОИПЛУМСРФДВБbЕЖНТХЦЧШЩЪЫЬЭЮЯА")
    return alphabet, substitution_list

def encrypt(text):
    alphabet, substitution_list = initialize_substitution_lists()
    used_chars = {}  # Словарь для отслеживания уже зашифрованных символов
    encrypted_text = []  # Список для зашифрованного текста
    shuffle_steps = []  # Список для сохранения перестановок

    print("Алфавит:", ''.join(alphabet))
    print("Начальный список подстановки:", ''.join(substitution_list))
    print("\nШаги шифрования:")

    for char in text:
        char_index = alphabet.index(char)  # Находим индекс символа в алфавите
        
        if char not in used_chars:
            # Символ встречается впервые
            substitute_char = substitution_list[char_index]
            used_chars[char] = substitute_char
            encrypted_text.append(substitute_char)
            shuffle_steps.append(None)  # Для первого вхождения добавляем None
            print(f"\nСимвол '{char}' встречается впервые. Заменяем на '{substitute_char}'.")
        else:
            # Символ уже встречался, генерируем случайное число R
            r = random.randint(1, len(alphabet) - 1)
            
            # Переставляем R-й и текущий символы в списке подстановки
            substitution_list[char_index], substitution_list[r] = substitution_list[r], substitution_list[char_index]
            
            # Заменяем символ на новый символ из списка подстановки на позиции R
            substitute_char = substitution_list[char_index]  # Используем заменённый символ
            encrypted_text.append(substitute_char)
            shuffle_steps.append((char_index, r))  # Сохраняем перестановку для дешифровки
            print(f"\nСимвол '{char}' уже встречался. Генерируем случайное число R = {r}.")
            print(f"Меняем местами символы на позициях {char_index} и {r} в списке подстановки.")
            print(f"Текущий список подстановки: {''.join(substitution_list)}")
            print(f"Заменяем символ '{char}' на '{substitute_char}'.")

    print("\nЗашифрованный текст:", ''.join(encrypted_text))
    return ''.join(encrypted_text), shuffle_steps

def decrypt(encrypted_text, shuffle_steps):
    alphabet, substitution_list = initialize_substitution_lists()
    decrypted_text = []

    print("\nШаги дешифровки:")

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        shuffle_step = shuffle_steps[i]

        if shuffle_step is None:
            # Первый раз встречавшийся символ
            char_index = substitution_list.index(char)
            decrypted_text.append(alphabet[char_index])
            print(f"\nСимвол '{char}' встречается впервые. Заменяем на '{alphabet[char_index]}'.")
        else:
            # Применяем обратную перестановку
            char_index, r = shuffle_step
            
            # Восстанавливаем перестановку
            substitution_list[char_index], substitution_list[r] = substitution_list[r], substitution_list[char_index]
            # Заменяем символ на символ из алфавита
            char_index = substitution_list.index(char)
            decrypted_text.append(alphabet[char_index])
            print(f"\nВосстанавливаем перестановку для символа '{char}'.")
            print(f"Меняем местами символы на позициях {char_index} и {r} в списке подстановки.")
            print(f"Текущий список подстановки: {''.join(substitution_list)}")
            print(f"Заменяем символ '{char}' на '{alphabet[char_index]}'.")
    
    # Переворачиваем список, так как дешифрование шло в том же порядке
    print("\nДешифрованный текст:", ''.join(decrypted_text))
    return ''.join(decrypted_text)

# Запрос исходного текста у пользователя
text = input("Введите исходный текст для шифрования: ")
encrypted_text, shuffle_steps = encrypt(text)
decrypted_text = decrypt(encrypted_text, shuffle_steps)
