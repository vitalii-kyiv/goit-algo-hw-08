import heapq

def heap_sort(iterable):
    """
    Виконує пірамідальне сортування списку за допомогою мін-купи.
    
    :param iterable: Ітерований об'єкт (список чисел)
    :return: Відсортований список
    """
    heap = list(iterable)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]

def min_cable_connection_cost(cables):
    """
    Знаходить мінімальні витрати на з'єднання кабелів шляхом об'єднання
    двох найменших кабелів у мін-купі на кожному кроці.
    
    :param cables: Список довжин кабелів
    :return: Мінімальні загальні витрати на з'єднання
    """
    heapq.heapify(cables)
    total_cost = 0
    
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
arr = [5, 3, 8, 1, 2, 7]
sorted_arr = heap_sort(arr)
print("Відсортований масив:", sorted_arr)

cables = [4, 3, 2, 6]
min_cost = min_cable_connection_cost(cables)
print("Мінімальні витрати на з'єднання кабелів:", min_cost)
