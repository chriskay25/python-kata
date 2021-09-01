def sort_array(src):
    srtd = sorted([i for i in src if i % 2 != 0])
    idx = 0
    for src_idx, num in enumerate(src):
        if num % 2 != 0:
            src[src_idx] = srtd[idx]
            idx = idx + 1
    print(src)

sort_array([5, 3, 2, 8, 1, 4])