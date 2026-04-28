import numpy as np

def task_1():
    """Створює масив від 10 до 19 та обчислює статистику."""
    arr = np.arange(10, 20)
    return {
        'sum': np.sum(arr),
        'mean': np.mean(arr),
        'min': np.min(arr),
        'max': np.max(arr)
    }

def task_2():
    """Створює масив з 1000 випадкових float64 та обчислює статистику."""
    arr = np.random.rand(1000).astype(np.float64)
    return {
        'sum': np.sum(arr),
        'mean': np.mean(arr),
        'min': np.min(arr),
        'max': np.max(arr)
    }

def task_3():
    """Робота з матрицею 5x5: вибір 2-го стовпця, 2-го рядка та flatten."""
    arr = np.random.randint(0, 100, size=(5, 5))
    second_col = arr[:, 1]
    second_row = arr[1, :]
    flattened = arr.flatten()
    return {
        'original': arr,
        'second_col': second_col,
        'second_row': second_row,
        'flattened': flattened
    }

def task_4():
    """Обчислення статистики для 500,000 випадкових чисел float64."""
    arr = np.random.random(500000).astype(np.float64)
    return {
        'sum': np.sum(arr),
        'mean': np.mean(arr),
        'min': np.min(arr),
        'max': np.max(arr)
    }

if __name__ == "__main__":
    print("=== Завдання 1: Масив 10-19 ===")
    res1 = task_1()
    print(f"Сума: {res1['sum']}, Середнє: {res1['mean']}, Мін: {res1['min']}, Макс: {res1['max']}")

    print("\n=== Завдання 2: 1000 випадкових float64 ===")
    res2 = task_2()
    print(f"Сума: {res2['sum']:.2f}, Середнє: {res2['mean']:.4f}, Мін: {res2['min']:.6f}, Макс: {res2['max']:.6f}")

    print("\n=== Завдання 3: Матриця 5x5 та зрізи ===")
    res3 = task_3()
    print("Матриця:\n", res3['original'])
    print(f"Другий стовпець: {res3['second_col']}")
    print(f"Другий рядок: {res3['second_row']}")
    print(f"Flattened (перші 10): {res3['flattened'][:10]}...")

    print("\n=== Завдання 4: 500,000 випадкових чисел ===")
    res4 = task_4()
    print(f"Сума: {res4['sum']:.2f}")
    print(f"Середнє: {res4['mean']:.4f}")
    print(f"Мінімум: {res4['min']:.6f}")
    print(f"Максимум: {res4['max']:.6f}")
