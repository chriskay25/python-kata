def scroll_section(scroll, sizes):
    for i in range(len(sizes)):
        if scroll < sum(sizes[:i + 1]): print(i)
    print(-1)

scroll_section(299, [300, 200, 400, 600, 100])