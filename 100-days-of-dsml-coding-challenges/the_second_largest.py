def find_second_largest(arr):
    unique_elements = sorted(set(arr))
    second_largest = unique_elements[-2]
    return second_largest

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    result = find_second_largest(arr)
    print(f"The second largest element is: {result}") 