проверь 
и приведи примеры реализации на библиотечных функциях 
# Классификационные метрики: каждый правильный ответ даёт 1 балл

def precision_at_1() -> float:
    users = [
        [1, 0, 0, 0, 0, 1], 
        [0, 1, 0, 0, 0, 1], 
        [0, 0, 1, 0, 0, 1]
    ]
    U = len(users)
    pres = sum(map(lambda user: user[0], users))
    return pres/U
    raise NotImplementedError()
    return ans

def precision_at_5() -> float:
    users = [
        [1, 0, 0, 0, 0, 1], 
        [0, 1, 0, 0, 0, 1], 
        [0, 0, 1, 0, 0, 1]
    ]
    U = len(users)
    precs = []
    for user in users:
      prec = sum(user[:5])/5
      precs.append(prec)
    return sum(precs)/U
    raise NotImplementedError()
    return ans

def recall_at_1() -> float:
    users = [
        [1, 0, 0, 0, 0, 1], 
        [0, 1, 0, 0, 0, 1], 
        [0, 0, 1, 0, 0, 1]
    ]
    U = len(users)
    recs = []
    for user in users:
      rec = user[0]/sum(user)
      recs.append(rec)
    return sum(recs)/U
    raise NotImplementedError()
    return ans
# Выводим результаты
for r in results:
    print(f"{r.metric}@{r.k} = {r.value:.4f}")



# Ранжирующие метрики: каждый правильный ответ даёт 1 балл

# AveragePrecision@3 для юзера `2`
def ap_at_3_for_user_2() -> float:
    users = [
        [1, 0, 0, 0, 0, 1], 
        [0, 1, 0, 0, 0, 1], 
        [0, 0, 1, 0, 0, 1]
    ]
    rel3 = users[1][:3]
    precs = []
    for i, item in enumerate(rel3):
      if item==1:
        prec = sum(rel3[:(i+1)])/(i+1)
        precs.append(prec)
    return sum(precs)/3
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

# DiscountedCumulativeGain@3 для юзера `2`
def dcg_at_3_for_user_2() -> float:
    users = [
        [1, 0, 0, 0, 0, 1], 
        [0, 1, 0, 0, 0, 1], 
        [0, 0, 1, 0, 0, 1]
    ]
    rel3 = users[1][:3]
    dcg = 0.0
    for i in range(0, len(rel3)):
        res = rel3[i]/np.log2(i+2)
        dcg+=res
    return dcg

    raise NotImplementedError()
    return ans

# IdealDiscountedCumulativeGain@3 для юзера `2`
def idcg_at_3_for_user_2() -> float:
    users = [
        [1, 0, 0, 0, 0, 1], 
        [0, 1, 0, 0, 0, 1], 
        [0, 0, 1, 0, 0, 1]
    ]
    user = users[1]
    limit = min(sum(user), 3)
    idcg = 0.0
    #минимальное из (2 (релевантных), 3 (@3) ) - это 2
    for i in range(1, limit+1):
      idcg += 1/np.log2(i+1)
    return idcg
    raise NotImplementedError()
    return ans

# NormalizedDiscountedCumulativeGain@3
def ndcg_at_3() -> float:
    idcg = idcg_at_3_for_user_2()
    dcg = dcg_at_3_for_user_2()
    return dcg/idcg if idcg>0 else 0.0
    raise NotImplementedError()
    return ans