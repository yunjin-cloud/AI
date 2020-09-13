def comb(lst,n):
   ret = []
   if n > len(lst): return ret

   if n == 1:
      for i in lst:
         ret.append([i])
   elif n>1:
      for i in range(len(lst)-n+1):
         for temp in comb(lst[i+1:],n-1):
            ret.append([lst[i]]+temp)

   return ret

def delete(lst): #중복 삭제
    new = []

    for i in lst:
        if i not in new:
            new.append(i)

    return new

def print_rst(lst):
    trst = []
    for i in range(1, len(lst)+1, 1):
        rst = []
        rst = comb(lst,i)
        rst = delete(rst)
        trst.append(rst) #진짜 남은 애들
    print(trst)

""" 입력
if __name__ == "__main__":

    arr = [1,1,2,3,4]
    print_rst(arr)
"""
