import re

def validar_cpf(cpf: str) -> bool:
    """
    Valida CPF brasileiro:
    - extrai apenas dígitos
    - rejeita CPFs com todos os dígitos iguais
    - confere os dois dígitos verificadores
    Retorna True/False.
    """
    if not isinstance(cpf, str):
        return False

    digitos = re.findall(r"\d", cpf)
    if len(digitos) != 11:
        return False

    nums = list(map(int, digitos))

    # Rejeita sequências do tipo 111.111.111-11
    if len(set(nums)) == 1:
        return False

    # 1º DV
    soma1 = sum(a * b for a, b in zip(nums[:9], range(10, 1, -1)))
    d1 = (soma1 * 10) % 11
    d1 = 0 if d1 == 10 else d1
    if d1 != nums[9]:
        return False

    # 2º DV
    soma2 = sum(a * b for a, b in zip(nums[:10], range(11, 1, -1)))
    d2 = (soma2 * 10) % 11
    d2 = 0 if d2 == 10 else d2
    return d2 == nums[10]