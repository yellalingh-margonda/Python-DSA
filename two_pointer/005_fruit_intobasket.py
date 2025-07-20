def max_profit(arr, k):
    l, n, maxi = 0, len(arr), 0
    hast_set={}
    for r in range(n):
        hast_set[arr[r]]=hast_set.get(arr[r],0)+1
        while len(hast_set.keys())>k:
            hast_set[arr[l]] = hast_set[arr[l]]-1
            if hast_set[arr[l]] == 0:
                del hast_set[arr[l]]
            l+=1
        maxi=max(maxi,r-l+1)
    return  maxi

fruits = [0,1,2,2]
print(max_profit(fruits,2))


def max_profit(arr, k):
    l = 0
    n = len(arr)
    curr_sum = 0
    max_sum = 0
    freq = {}

    for r in range(n):
        freq[arr[r]] = freq.get(arr[r], 0) + 1
        curr_sum += arr[r]

        while len(freq) > k:
            freq[arr[l]] -= 1
            curr_sum -= arr[l]
            if freq[arr[l]] == 0:
                del freq[arr[l]]
            l += 1

        max_sum = max(max_sum, curr_sum)

    return max_sum

def max_fruit_brute(arr, k):
    maxi,n=0, len(arr)
    for i in range(n):
        temp=set()
        for j in range(i, n):
            if len(temp)>2:
                break
            temp.add(arr[j])
            maxi=max(maxi, j-i+1)
    return  maxi

fruits = [0,1,2,2]
print(max_fruit_brute(fruits,2))
