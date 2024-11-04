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
            print(f"\nСимвол '{char}' встречается впервые. Заменяем на '{substitute_char}'.")
        else:
            # Символ уже встречался, генерируем случайное число R
            r = random.randint(1, len(alphabet) - 1)
            
            # Переставляем R-й и текущий символы в списке подстановки
            substitution_list[char_index], substitution_list[r] = substitution_list[r], substitution_list[char_index]
            
            # Заменяем символ на новый символ из списка подстановки на позиции R
            substitute_char = substitution_list[r]
            encrypted_text.append(substitute_char)
            print(f"\nСимвол '{char}' уже встречался. Генерируем случайное число R = {r}.")
            print(f"Меняем местами символы на позициях {char_index} и {r} в списке подстановки.")
            print(f"Текущий список подстановки: {''.join(substitution_list)}")
            print(f"Заменяем символ '{char}' на '{substitute_char}'.")

    print("\nЗашифрованный текст:", ''.join(encrypted_text))
    return ''.join(encrypted_text)

# Запрос исходного текста у пользователя
text = input("Введите исходный текст для шифрования: ")
encrypted_text = encrypt(text)
