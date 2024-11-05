import random

def shuffle_text(text, iterations=3):
    # Преобразуем текст в список символов
    characters = list(text)
    
    print("Исходный текст:", text)
    shuffle_indices = []  # Список для хранения индексов перемешивания

    for i in range(iterations):
        # Генерируем порядок индексов и сохраняем его
        indices = list(range(len(characters)))
        random.shuffle(indices)
        shuffle_indices.append(indices)
        
        # Применяем перемешивание с сохраненным порядком индексов
        characters = [characters[idx] for idx in indices]
        shuffled_text = ''.join(characters)
        print(f"Перемешивание {i}: {shuffled_text}")

    # Финальный зашифрованный текст после всех итераций
    encrypted_text = ''.join(characters)
    print("\nЗашифрованный текст:", encrypted_text)
    return encrypted_text, shuffle_indices

def unshuffle_text(encrypted_text, shuffle_indices):
    characters = list(encrypted_text)

    # Применяем обратное перемешивание
    for i in range(len(shuffle_indices) - 1, -1, -1):
        indices = shuffle_indices[i]
        
        # Создаём массив для обратного восстановления
        unshuffled_characters = [None] * len(characters)
        for original_idx, shuffled_idx in enumerate(indices):
            unshuffled_characters[shuffled_idx] = characters[original_idx]
        
        characters = unshuffled_characters
        print(f"Обратное перемешивание {len(shuffle_indices) - i}: {''.join(characters)}")

    decrypted_text = ''.join(characters)
    print("\nРасшифрованный текст:", decrypted_text)
    return decrypted_text

# Запрос исходного текста у пользователя
text = input("Введите текст для шифрования: ")
iterations = int(input("Введите количество итераций перемешивания: "))

# Шифруем текст и сохраняем порядок перемешиваний
encrypted_text, shuffle_indices = shuffle_text(text, iterations)

# Расшифровываем текст с использованием сохраненного порядка
decrypted_text = unshuffle_text(encrypted_text, shuffle_indices)
