def restaParesImpares(arr):
    if len(arr) > 0:
        return resta(arr, len(arr) - 1)
    else:
        return 0


def resta(arr, x) -> int:
    if x == 0:
        if arr[0] % 2 == 0:
            return arr[0]
        else:
            return -arr[0]
    else:
        if arr[x] % 2 == 0:
            return arr[x] + resta(arr, x - 1)
        else:
            return -arr[x] + resta(arr, x - 1)
        
lista = [8, 6, 7, 5]
z = restaParesImpares(lista)
print(z)