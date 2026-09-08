def calculate_bmi(weight : float, height : float) -> float:
    '''
    Calcula el índice de masa corporal (IMC)

    Params:
    - weight : Peso expresado en kilogramos.
    - height: Altura expresada en metros.

    Return:
    - Devuelve el IMC según la tabla de la OMS
    '''
    imc = weight / (height ** 2)
    return imc