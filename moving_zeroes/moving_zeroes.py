'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    x = 0

    for i in arr:
        if i:
            arr[x] = i
            x = x + 1
    
    for i in range(x, len(arr)):
        arr[i] = 0


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")