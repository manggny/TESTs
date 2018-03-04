#-*-coding: UTF-8-*-
def min_list(LIST):                          # 리스트를 input 했을때, 가장 작을수를 첫번째 원소로 배열시키는 함수.
    for i in range(len(LIST)):               # 방법 :  1. 리스트 중에서 가장작은 수를 찾는다-> 0번째 원소로 놓는다
        Min = LIST[i]					     #         2. 0번째 원소를 제외한 원소중에서 가장 작은 수를 찾는다 -> 1번째 원소로 놓는다 
        index = i                            #         3. 0~1번째 원소를 제외한 원소중에서 가장 작은 수를 찾는다 -> 2번째 원소로 놓는다
        for ii in range((i+1),len(LIST)):    #         .
            if(Min > LIST[ii]):              #         .
                Min = LIST[ii]               #         N. 0~(N-2)번째 원소를 제외한 원소중에서 가장 작은수를 찾는다 -> (N-1)번째 원소로 놓는다.
                index = ii
        temp = LIST[i]
        LIST[i] = Min
        LIST[index] = temp
    print(LIST)
    return LIST



def five(LIST):
    List=[]
    j = 0
    for i in range(len(LIST)):
        if(LIST[i] % 5 ==0):
            List.append(LIST[i])
    print(List)
    return List


def main():
    a = [125,421,327,380,728,645]
    List = min_list(a)
    List_five = five(List)


if __name__=="__main__":
    main()
    


