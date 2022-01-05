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
    values = set()
    for c in range(p+1):
        try:

            k,l = map(int,input().split())
            pairs.append((k,l))
            values.add(k)
            values.add(l)
            males.append(k)
            females.append(l)
        except:
            continue
    fam = get_family(pairs)
   # print(fam)
    if len(values) != n:
        values = range(1,n+1)
    invalid_pairs = get_combinations(fam)
    total_pairs = set(itertools.combinations(sorted(list(values)),2))
    male_pair = set(itertools.combinations(sorted(list(males)),2))
    female_pair = set(itertools.combinations(sorted(list(females)),2))

    valid_pairs = total_pairs - invalid_pairs - male_pair - female_pair
    

    print(len(valid_pairs))
