import numpy as np
from sklearn.metrics import precision_score, recall_score, average_precision_score, dcg_score, ndcg_score

# Исходные данные
users = np.array([
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1], 
    [0, 0, 1, 0, 0, 1]
])
scores = np.array([
    [0.9, 0.4, 0.3, 0.2, 0.1, 0.8],
    [0.4, 0.9, 0.3, 0.2, 0.1, 0.8],
    [0.3, 0.4, 0.9, 0.2, 0.1, 0.8]
])

# Вычисление метрик
metrics = {
    "Precision@1": precision_score(users[:, 0], np.ones(len(users))),
    "Precision@5": np.mean([precision_score(u[:5], np.ones(5)) for u in users]),
    "Recall@1": recall_score(users[:, 0], np.ones(len(users))),
    "AP@3 User1": average_precision_score(users[1, :3], scores[1, :3]),
    "MAP@3": np.mean([average_precision_score(u[:3], s[:3]) for u, s in zip(users, scores)]),
    "DCG@3 User1": dcg_score([users[1, :3]], [scores[1, :3]]),
    "NDCG@3 User1": ndcg_score([users[1, :3]], [scores[1, :3]], k=3)
}

# Вывод результатов
for name, value in metrics.items():
    print(f"{name}: {value:.4f}")