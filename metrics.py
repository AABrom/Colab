import numpy as np
from sklearn.metrics import precision_score, recall_score, average_precision_score, dcg_score, ndcg_score

# Данные для всех метрик
users = [
    [1, 0, 0, 0, 0, 1],  # Юзер 0
    [0, 1, 0, 0, 0, 1],  # Юзер 1 (в вашем коде это "юзер 2" из-за 0-based индексации)
    [0, 0, 1, 0, 0, 1]   # Юзер 2
]
scores = [
    [0.9, 0.4, 0.3, 0.2, 0.1, 0.8],  # Скоры для юзера 0
    [0.4, 0.9, 0.3, 0.2, 0.1, 0.8],  # Скоры для юзера 1
    [0.3, 0.4, 0.9, 0.2, 0.1, 0.8]   # Скоры для юзера 2
]

# 1. Precision@1 (по первому документу для всех юзеров)
precision_1 = precision_score(
    y_true=[u[0] for u in users],
    y_pred=[1]*len(users)  # Предполагаем, что всегда возвращаем документ на первой позиции
)

# 2. Precision@5 (по топ-5 документов)
precision_5 = np.mean([
    precision_score(u[:5], [1]*5) for u in users
])

# 3. Recall@1 (по первому документу)
recall_1 = recall_score(
    y_true=[u[0] for u in users],
    y_pred=[1]*len(users)
)

# 4. AP@3 для юзера 1 (в вашем коде он называется "юзер 2")
ap_3_user1 = average_precision_score(
    y_true=users[1][:3],
    y_score=scores[1][:3]
)

# 5. MAP@3 (среднее AP@3 по всем юзерам)
map_3 = np.mean([
    average_precision_score(u[:3], s[:3]) 
    for u, s in zip(users, scores)
])

# 6. DCG@3 для юзера 1
dcg_3_user1 = dcg_score(
    y_true=[users[1][:3]],
    y_score=[scores[1][:3]]
)

# 7. IDCG@3 для юзера 1 (вручную, так как в sklearn нет прямой функции)
ideal_order = sorted(users[1][:3], reverse=True)
idcg_3_user1 = dcg_score([ideal_order], [sorted(scores[1][:3], reverse=True)])

# 8. NDCG@3 для юзера 1
ndcg_3_user1 = ndcg_score(
    y_true=[users[1][:3]],
    y_score=[scores[1][:3]],
    k=3
)

# Вывод всех результатов
print("Библиотечные метрики:")
print(f"Precision@1: {precision_1:.4f}")
print(f"Precision@5: {precision_5:.4f}")
print(f"Recall@1: {recall_1:.4f}")
print(f"AP@3 для юзера 1: {ap_3_user1:.4f}")
print(f"MAP@3: {map_3:.4f}")
print(f"DCG@3 для юзера 1: {dcg_3_user1:.4f}")
print(f"IDCG@3 для юзера 1: {idcg_3_user1:.4f}")
print(f"NDCG@3 для юзера 1: {ndcg_3_user1:.4f}")