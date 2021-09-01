import itertools

def best_travel(t, k, ls):
    diffs, sums = [], []
    combos = set(itertools.combinations(ls, k))
    for c in combos:
        if sum(c) <= t: 
            sums.append(sum(c))
            diffs.append(t - sum(c))
    closest = min(diffs)
    idx = diffs.index(closest)
    return sums[idx]

best_travel(230, 4, [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89])

# SMARTER WAY

# def choose_best_sum(t, k, ls):
#     try: 
#         return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
#     except:
#         return None