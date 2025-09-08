def multiply_matrices(A, B):
    """
    Multiplica A (m x n) por B (n x p).
    Verifica:
    - A e B não vazias
    - retangularidade
    - compatibilidade de dimensões
    """
    if not A or not B or not isinstance(A, list) or not isinstance(B, list):
        raise ValueError("Matrizes devem ser listas não vazias")

    m = len(A)
    n = len(A[0])
    if any(len(row) != n for row in A):
        raise ValueError("Matriz A não é retangular")

    p = len(B[0])
    if any(len(row) != p for row in B):
        raise ValueError("Matriz B não é retangular")

    if len(B) != n:
        raise ValueError("Dimensões incompatíveis para multiplicação")

    res = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            res[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return res

def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

