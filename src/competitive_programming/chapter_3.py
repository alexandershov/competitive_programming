def binary_function(n):
    yield f'binary_function({n})'
    if n == 1:
        return
    yield from binary_function(n - 1)
    yield from binary_function(n - 1)
