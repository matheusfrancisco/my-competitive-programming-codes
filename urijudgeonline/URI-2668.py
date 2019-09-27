# -*- coding: utf-8 -*-


MODULO = 10 ** 4


def matrix_mult(A, B):
    R = [[0, 0],
         [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                R[i][j] += (A[i][k] * B[k][j]) % MODULO
    return R


def fast_exp(M, n):
    R = [[1, 0],
         [0, 1]]
    while n > 0:
        if (n % 2) == 1:
            R = matrix_mult(R, M)
        M = matrix_mult(M, M)
        n = n // 2
    return R


def f(a, b, n):
    alfa = 2 * a
    beta = b - a ** 2

    M = [[alfa, beta],
         [1, 0]]
    R = fast_exp(M, n)
    return (R[1][0] * 2 * a + R[1][1] * 2) % MODULO


A, B, N, K = map(int, input().split())
res = f(A, B, N)

if ((A * A) != B) and (((N % 2) == 0) or ((A * A) > B)):
    res = (res - 1) % MODULO

res = "%04d" % res
print(res[len(res) - K])
