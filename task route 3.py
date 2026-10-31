import numpy as np
arr = np.random.randint(1, 101, (3, 3))
print("Original Array:")
print(arr)
normalized = (arr - arr.min()) / (arr.max() - arr.min())
print("Normalized Array:")
print(normalized)
arr = np.random.randint(1, 101, 10)
print("\nArray:")
print(arr)
x = int(input("Enter X: "))
closest = arr[np.abs(arr - x).argmin()]

print("Closest Value:", closest)

arr = np.random.randint(1, 101, (5, 5))
print("\nOriginal Array:")
print(arr)

second_largest = np.sort(arr, axis=0)[-2]
print("Second Largest in Each Column:")
print(second_largest)

arr = np.random.randint(1, 101, (6, 4))
print("\nMatrix:")
print(arr)

row_sums = arr.sum(axis=1)
even_rows = np.where(row_sums % 2 == 0)[0]

print("Rows with Even Sum:")
print(even_rows)

arr = np.random.randint(1, 51, 30)
print("\nOriginal Array:")
print(arr)

arr[(arr % 3 == 0) | (arr % 5 == 0)] = -1

print("Modified Array:")
print(arr)

arr = np.random.randint(1, 101, (3, 3))
print("\nOriginal Array:")
print(arr)

row_means = arr.mean(axis=1, keepdims=True)
result = arr - row_means

print("Array After Subtracting Row Means:")
print(result)