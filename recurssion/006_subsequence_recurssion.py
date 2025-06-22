# subsequence([1,2,3], path=[], index=0)
# ├── Include 1 → path=[1]
# │   ├── Include 2 → path=[1,2]
# │   │   ├── Include 3 → path=[1,2,3] → ✅ [1,2,3]
# │   │   └── Exclude 3 → path=[1,2]   → ✅ [1,2]
# │   └── Exclude 2 → path=[1]
# │       ├── Include 3 → path=[1,3]   → ✅ [1,3]
# │       └── Exclude 3 → path=[1]     → ✅ [1]
# └── Exclude 1 → path=[]
#     ├── Include 2 → path=[2]
#     │   ├── Include 3 → path=[2,3]   → ✅ [2,3]
#     │   └── Exclude 3 → path=[2]     → ✅ [2]
#     └── Exclude 2 → path=[]
#         ├── Include 3 → path=[3]     → ✅ [3]
#         └── Exclude 3 → path=[]      → ✅ []



def subsequence(array,path=None, index=None):
    if path is None:
        path = []
    if index==None:
        index=0
    if index>=len(array):
        return [path[:]]
    path.append(array[index])
    left=subsequence(array,path,index+1)
    path.pop(-1)
    right=subsequence(array, path, index + 1)
    return left+right

print(subsequence([1,2,3]))