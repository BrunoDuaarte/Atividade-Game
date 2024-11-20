def dividir(valor, divisor):
    try:
        return valor / divisor
    except ZeroDivisionError:
        return "Erro: Divisão por zero."
