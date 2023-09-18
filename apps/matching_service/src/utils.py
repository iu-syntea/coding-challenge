def calculate_jaccard_similarity(a: str, b: str) -> float:
    a_set = set([word.lower() for word in a.split(' ')])
    b_set = set([word.lower() for word in b.split(' ')])

    len_intersection = len(a_set.intersection(b_set))
    len_union = len(a_set.union(b_set))

    if len_union == 0:
        return 0.0
    return float(len_intersection / len_union)
