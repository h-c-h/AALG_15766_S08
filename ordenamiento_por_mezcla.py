def merge_sort(arr, nivel=0):
    indent = "  " * nivel  
    print(f"{indent}Dividiendo: {arr}")


    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half, nivel + 1)
    right_sorted = merge_sort(right_half, nivel + 1)

    merged = merge(left_sorted, right_sorted)
    print(f"{indent}Combinando: {left_sorted} + {right_sorted} => {merged}")
    return merged

def merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    return result

lista = [5, 2, 9, 1, 7, 3, 8]
print("Inicio del ordenamiento por mezcla (Merge Sort):")
ordenada = merge_sort(lista)
print("\nResultado final:")
print(ordenada)