def solution(participant, completion):
    dic = {}
    for part in participant:
        if part not in dic.keys():
            dic[part] = 1
        else:
            dic[part] += 1
                    
    for c in completion:
        dic[c] -= 1
                
    for key, value in dic.items():
        if value != 0:
            return key