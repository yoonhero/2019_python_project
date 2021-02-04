
def solution(name):
    abc_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    name = name.lower()
    length = len(abc_list)
    name_list = list(name)
    first = True
    count = 0
    num = 0
    index_num = []

    for names in name_list:
        index_num.append(abc_list.index(names)+1)
        
    index_num.sort()
    for i in range(0, len(index_num)):
        
    

solution("JAZ")