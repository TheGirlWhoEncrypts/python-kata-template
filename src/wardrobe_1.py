def wardrobe1(sizes, total):
    results = []

    if total == 0:
        return results

    def recursion(subset=[]):
        for s in sizes:
            if sum(subset + [s]) < total:
                recursion(subset + [s])
            elif sum(subset + [s]) == total:
                results.append(sorted(subset + [s]))

    recursion()
    return list(map(list, sorted(set(map(tuple, results)))))