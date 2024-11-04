import random

def shuffle_text(text, iterations=3):
    # Преобразуем текст в список символов
    characters = list(text)
    
    print("Исходный текст:", text)

    for i in range(iterations):
        # Случайным образом перемешиваем символы
        random.shuffle(characters)
        shuffled_text = ''.join(characters)
        print(f"Перемешивание {i + 1}: {shuffled_text}")

    # Финальный зашифрованный текст после всех итераций
    encrypted_text = ''.join(characters)
    print("\nЗашифрованный текст:", encrypted_text)
    return encrypted_text

# Запрос исходного текста у пользователя
text = input("Введите текст для шифрования: ")
iterations = int(input("Введите количество итераций перемешивания: "))
encrypted_text = shuffle_text(text, iterations)
