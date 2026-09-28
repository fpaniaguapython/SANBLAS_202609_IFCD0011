def sumar(sumando_1: int, sumando_2: int) -> int:
    assert isinstance(sumando_1, int), 'sumando_1 es erróneo'
    assert isinstance(sumando_2, int), 'sumando_2 es erróneo'
    return sumando_1 + sumando_2

print(sumar(5, '8'))