def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        bearing_element = array[int(len(array) / 2)]
        bigger_array = []
        equal_array = []
        less_array = []
    for i in range(len(array)):
        if array[i] == bearing_element:
            equal_array.append(array[i])
        if array[i] < bearing_element:
            less_array.append(array[i])
        if array[i] > bearing_element:
            bigger_array.append(array[i])
    if bearing_element % 2 == 0:
        return quick_sort(less_array) + equal_array + quick_sort(bigger_array)
    else:
        return quick_sort(bigger_array) + equal_array + quick_sort(less_array)


def modified_quick_sort(array):
    if (array):
        array_of_even_numbers = []
        array_of_odd_numbers = []
        for i in range(len(array)):
            if array[i] % 2 == 0:
                array_of_even_numbers.append(array[i])
            else:
                array_of_odd_numbers.append(array[i])
        return quick_sort(array_of_even_numbers) + quick_sort(array_of_odd_numbers)


def array_creation():
    print("Введите размер массива (1 < N < 10001):")
    size = int(input())
    print("Введите элементы массива через пробел:")
    array = list(map(int, input().split()))
    if (size != len(array)):
        print("Длина массива не совпадает с указанной длиной")
    else:
        return array


print(modified_quick_sort(array_creation()))
