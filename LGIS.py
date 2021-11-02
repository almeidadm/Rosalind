def print_LIS(arr):
    for x in arr:
        print(abs(x), end=" ")
    print()

def constructPrintLIS(arr: list, n: int):

# L[i] - The longest increasing sub-sequence
# ends with arr[i]
    l = [[] for i in range(n)]

    # L[0] is equal to arr[0]
    l[0].append(arr[0])

    # start from index 1
    for i in range(1, n):

        # do for every j less than i
        for j in range(i):

            # L[i] = {Max(L[j])} + arr[i]
            # where j < i and arr[j] < arr[i]
            if arr[i] > arr[j] and (len(l[i]) < len(l[j]) + 1):
                l[i] = l[j].copy()

         #L[i] ends with arr[i]
        l[i].append(arr[i])

    # L[i] now stores increasing sub-sequence of
    # arr[0..i] that ends with arr[i]
    maxx = l[0]

    # LIS will be max of all increasing sub-
    # sequences of arr
    for x in l:
        if len(x) > len(maxx):
            maxx = x

    # max will contain LIS
    print_LIS(maxx)
# This code is contributed by
# sanjeev2552

# Driver Code
if __name__ == "__main__":
    file = open('rosalind_lgis.txt', 'r').read().split("\n")[1].split(" ")[:-1]
    
    arr = [int(file[i]) for i in range(len(file))]
    n = len(arr)
    constructPrintLIS(arr, n)
    
    arr = [(-1)*arr[i] for i in range(n)]
    constructPrintLIS(arr, n)
    
# Adaptation to Rosalind problem by
# Diego de Almeida Miranda
