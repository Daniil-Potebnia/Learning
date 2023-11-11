def counter(elems, elem):
    count = 0
    for n in elems:
        if n == elem:
            count += 1
    return {f'count-{elem}': count}
