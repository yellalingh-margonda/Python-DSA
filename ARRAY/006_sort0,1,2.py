def dutch_sort(arr):
    #0 to low-1 are all zeros
    #low to mid-1 are all ones
    #high to n  are all twos
    #a[mid]==0 swap a[mid],a[low] mid++, low++
    #a[mid]==1 mid++
    #a[mid]==2 swap a[mid],a[high] high--
    l,m,h=0,0,len(arr)-1
    while m<h:
        if arr[m]==0:
            arr[m],arr[l]=arr[l],arr[m]
            m+=1
            l+=1
        elif arr[m]==1:
            m+=1
        else:
            arr[m],arr[h]=arr[h],arr[m]
            h-=1
    return arr
nums = [2,0,2,1,1,0]
print(dutch_sort(nums))

