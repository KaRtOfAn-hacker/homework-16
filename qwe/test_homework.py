import pytest
import numpy as np
from homework import task_1, task_2, task_3, task_4

def test_task_1():
    res = task_1()
    assert res['sum'] == sum(range(10, 20))
    assert res['mean'] == 14.5
    assert res['min'] == 10
    assert res['max'] == 19

def test_task_2():
    res = task_2()
    assert isinstance(res['sum'], np.float64)
    assert 0 <= res['min'] < res['max'] <= 1

def test_task_3():
    res = task_3()
    assert res['original'].shape == (5, 5)
    assert res['second_col'].shape == (5,)
    assert res['second_row'].shape == (5,)
    assert res['flattened'].shape == (25,)
    # Перевірка, що вибрані саме другий стовпець та рядок
    assert np.array_equal(res['second_col'], res['original'][:, 1])
    assert np.array_equal(res['second_row'], res['original'][1, :])

def test_task_4():
    res = task_4()
    assert isinstance(res['sum'], np.float64)
    # Для 500,000 чисел від 0 до 1 середня сума має бути близько 250,000
    assert 240000 < res['sum'] < 260000
    assert 0.49 < res['mean'] < 0.51
