def com_sum(array, index, target, path):
    if target==0:
        return [path[:]]
    if index>= len(array) or target<0:
        return []
    all_combination=[]
    for i in range(index+1, len(array)):
        if array[i]==array[i-1]:
            continue
        if array[i]>target:
            break
        path.append(array[i])
        left=com_sum(array,i+1,target-array[i],path)
        all_combination.extend(left)
        path.pop()
    return all_combination

#Left/Right: "For the element at current_index, do I use it or not?"
#for loop: "From the remaining elements starting at start_index, which one do I choose to be the next element in my combination?"