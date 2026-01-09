'''Given a list of non-negative numbers, find the first continuous subarray
whose sum equals the given target and return its 1-based positions.'''

def subarraySum(arr, target):
    left = 0
    current_sum = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1

        if current_sum == target:
            return [left + 1, right + 1]

    return [-1]

if __name__ == "__main__":
    arr = [1, 2, 3, 7, 5]
    target = 12
    result = subarraySum(arr, target)
    print(result) 