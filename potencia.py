def potencia(base, exponente):
    """
    Calcula la potencia de un número.

    Parámetros:
    base (int o float): número base
    exponente (int o float): número que indica la potencia

    Retorna:
    int o float: resultado de elevar la base al exponente

    Lanza:
    TypeError: si los valores no son numéricos
    """

    if not isinstance(base, (int, float)):
        raise TypeError("La base debe ser un número")

    if not isinstance(exponente, (int, float)):
        raise TypeError("El exponente debe ser un número")

    return base ** exponente