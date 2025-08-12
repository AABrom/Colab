def map_at_3_simple() -> float:
    users = [
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1]
    ]

    user_aps = []
    for user in users:
        rel3 = user[:3]
        precisions = []
        for i in range(1, 4):
            if rel3[i-1] == 1:
                p = sum(rel3[:i]) / i
                precisions.append(p)
        ap = sum(precisions) / len(precisions) if precisions else 0
        user_aps.append(ap)

    return sum(user_aps) / len(users)
