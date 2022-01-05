import itertools 

def get_family(pairs):

    set_list = set([frozenset(s) for s in pairs])  
    result = []
    while(set_list):                  
        new = set(set_list.pop())   
        check = len(set_list)           
        while check:                
            check = False
            for s in set_list.copy():
                if new.intersection(s):
                    check = True 
                    set_list.remove(s)
                    new.update(s)
        result.append(tuple(new))
    return result

def get_combinations(lis):
    f = ([set(itertools.combinations(i,2)) for i in lis])
    merged_set = set().union(*f)
    return merged_set

if __name__ == "__main__":

    n,p = map(int,input().split())
    pairs = []
    males = []
    females = []
    for c in range(p):
        k,l = map(int,input().split())
        pairs.append((k,l))
        males.append(k)
        females.append(l)
    fam = get_family(pairs)
   # print(fam)
    invalid_pairs = get_combinations(fam)
    total_pairs = set(itertools.combinations(range(1,n+1),2))
    male_pair = set(itertools.combinations(males,2))
    female_pair = set(itertools.combinations(females,2))

    valid_pairs = total_pairs - invalid_pairs - male_pair - female_pair

    print(len(valid_pairs))
