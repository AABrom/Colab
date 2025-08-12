# MeanAveragePrecision@3
def map_at_3() -> float:
    users = [
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1]
    ]

    user_aps = []
    for user in users:
        rel3 = user[:3]
        precs = []
        for i in range(1, 4):
            if rel3[i-1] == 1:
                p = sum(rel3[:i]) / i
                precs.append(p)
        ap = sum(precs) / len(precs)
        user_aps.append(ap)

    return sum(user_aps) / len(users)

    raise NotImplementedError()
    return ans


# MeanAveragePrecision@3
def map_at_3() -> float:
    users = [
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1]
    ]

    user_aps = []
    for user in users:
        rel3 = user[:3]
        precs = [sum(rel3[:i+1])/(i+1) for i in range(3) if rel3[i]==1]
        ap = sum(precs) / 3 if precs else 0.0
        user_aps.append(ap)
    return sum(user_aps) / len(users)

    raise NotImplementedError()
    return ans
