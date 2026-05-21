import numpy as np

# Завдання 1
print("--- Завдання 1 ---")

# Створюємо три масиви 4х4 з числами від -10 до 10
array1 = np.random.randint(-10, 11, (4, 4))
array2 = np.random.randint(-10, 11, (4, 4))
array3 = np.random.randint(-10, 11, (4, 4))

# Об'єднуємо їх за допомогою np.stack
combined_array = np.stack((array1, array2, array3))

# Виводимо результат
print("Об'єднаний масив з новою віссю:\n", combined_array)

# Перевірка розміру
assert combined_array.shape == (3, 4, 4), "Розмір об'єднаного масиву повинен бути (3, 4, 4)"
print("\n")


# Завдання 2
print("--- Завдання 2 ---")

B = np.random.randint(1, 10, (2, 3, 4))
print("Оригінальний тривимірний масив B:\n", B)

# Змінюємо форму у двовимірний 6х4
B_reshaped = B.reshape(6, 4)
print("Масив після зміни форми:\n", B_reshaped)

# Робимо "сплющення" (перетворення у одновимірний)
B_flattened = B_reshaped.flatten()
print("Одновимірний масив:\n", B_flattened)
print("\n")


# Завдання 3
print("--- Завдання 3 ---")

C = np.random.randint(1, 10, (3, 3, 3))
print("Оригінальний масив C:\n", C)

# Сума по першій осі (0)
sum_axis0 = C.sum(axis=0)
print("Сума по осі 0:\n", sum_axis0)

# Сума по другій осі (1)
sum_axis1 = C.sum(axis=1)
print("Сума по осі 1:\n", sum_axis1)

# Загальна сума
total_sum = C.sum()
print("Загальна сума елементів масиву:", total_sum)
