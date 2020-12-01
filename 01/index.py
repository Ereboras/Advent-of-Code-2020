def find_two_sum(arr, arr_size, sum):
    for i in range(0, arr_size):
        currentN = arr[i]

        for y in range(i+1, arr_size):
            testedN = arr[y]

            if currentN + testedN == sum:
                return currentN*testedN
    return -1

def find_three_sum(arr, arr_size, sum):
    for i in range(0, arr_size):
        s = set()
        new_sum = sum - arr[i]
        for y in range(i+1, arr_size):
            if new_sum - arr[y] in s:
                return arr[i]*arr[y]*(new_sum-arr[y])
            s.add(arr[y])
    return -1

f = open('data.txt', 'r')
l = f.read().split('\n')
l.remove('')
l = list(map(int, l))


print(find_two_sum(l, len(l), 2020))
print(find_three_sum(l, len(l), 2020))