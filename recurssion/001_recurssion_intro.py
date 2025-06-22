
def print_fun_afterbacktrack(count):
    if count==4:
        return
    count+=1
    print_fun_afterbacktrack(count)
    print(f"count after backtrack:{count}")

def print_fun_beforebacktrack(count):
    if count==4:
        return
    count+=1
    print(f"count before backtrack:{count}")
    print_fun_beforebacktrack(count)


print_fun_beforebacktrack(count=0)
print(f"*********")
print_fun_afterbacktrack(count=0)
#Recurssion function calling itsefl
#base case stoping from infinite recurssion
#stack over flow when infite recurssion
