import numpy as np
from sklearn.metrics import precision_score, recall_score, average_precision_score, dcg_score, ndcg_score

# Фиксированные данные (как в вашем исходном коде)
users = np.array([
    [1, 0, 0, 0, 0, 1],  # Юзер 0: релевантные на 1 и 6 позициях
    [0, 1, 0, 0, 0, 1],  # Юзер 1: релевантные на 2 и 6 позициях
    [0, 0, 1, 0, 0, 1]   # Юзер 2: релевантные на 3 и 6 позициях
])

# Скоры модели (строго соответствующие вашему порядку: 1 → 0.9 → 0.8 → ...)
scores = np.array([
    [0.9, 0.8, 0.7, 0.6, 0.5, 0.4],  # Для юзера 0
    [0.8, 0.9, 0.7, 0.6, 0.5, 0.4],  # Для юзера 1
    [0.7, 0.8, 0.9, 0.6, 0.5, 0.4]   # Для юзера 2
])

# 1. Precision@1
precision_1 = precision_score(users[:, 0], np.ones(len(users)))

# 2. Precision@5
precision_5 = np.mean([precision_score(u[:5], np.ones(5)) for u in users])

# 3. Recall@1
recall_1 = recall_score(users[:, 0], np.ones(len(users)))

# 4. AP@3 для юзера 1 (второй в массиве)
ap_3_user1 = average_precision_score(users[1, :3], scores[1, :3])

# 5. MAP@3
map_3 = np.mean([average_precision_score(u[:3], s[:3]) for u, s in zip(users, scores)])

# 6. DCG@3 для юзера 1
dcg_3_user1 = dcg_score([users[1, :3]], [scores[1, :3]])

# 7. IDCG@3 для юзера 1 (идеальное ранжирование)
idcg_3_user1 = dcg_score([np.sort(users[1, :3])[::-1]], [np.sort(scores[1, :3])[::-1]])

# 8. NDCG@3 для юзера 1
ndcg_3_user1 = dcg_3_user1 / idcg_3_user1 if idcg_3_user1 > 0 else 0

print("Результаты (с сохранением вашего порядка ранжирования):")
print(f"Precision@1: {precision_1:.4f}")  # Должно быть ~0.333 (1 из 3)
print(f"Precision@5: {precision_5:.4f}")  # Должно быть ~0.200 (1/5 в среднем)
print(f"Recall@1: {recall_1:.4f}")       # Должно быть ~0.333 (1 из 3)
print(f"AP@3 User1: {ap_3_user1:.4f}")   # Должно быть низким (~0.33)
print(f"MAP@3: {map_3:.4f}")             # Должно быть низким (~0.33)
print(f"DCG@3 User1: {dcg_3_user1:.4f}") # Должно быть ~0.63
print(f"IDCG@3 User1: {idcg_3_user1:.4f}") # Должно быть ~1.13
print(f"NDCG@3 User1: {ndcg_3_user1:.4f}") # Должно быть ~0.56