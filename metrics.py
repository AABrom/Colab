import numpy as np
from sklearn.metrics import precision_score, recall_score, average_precision_score, dcg_score, ndcg_score

# Текущее ранжирование модели (как в вашем коде)
users_model = np.array([
    [1, 0, 0, 0, 0, 1],  # Релевантные на 1 и 6 позициях (плохо!)
    [0, 1, 0, 0, 0, 1],  # Релевантные на 2 и 6
    [0, 0, 1, 0, 0, 1]   # Релевантные на 3 и 6
])

# Идеальное ранжирование (все 1 в начале)
users_ideal = np.array([
    [1, 1, 0, 0, 0, 0],  # Релевантные на 1 и 2 позициях
    [1, 1, 0, 0, 0, 0],  # Идеал для всех юзеров
    [1, 1, 0, 0, 0, 0]
])

# Скоры модели (соответствуют текущему ранжированию)
scores_model = np.array([
    [0.9, 0.4, 0.3, 0.2, 0.1, 0.8],  # 1-я позиция: 0.9 (релевантна), 6-я: 0.8 (релевантна)
    [0.4, 0.9, 0.3, 0.2, 0.1, 0.8],  # 2-я позиция: 0.9
    [0.3, 0.4, 0.9, 0.2, 0.1, 0.8]   # 3-я позиция: 0.9
])

# Метрики для текущего ранжирования (сравнение с идеалом)
metrics = {
    # Precision/Recall считаем для первого релевантного документа
    "Precision@1": precision_score(users_ideal[:, 0], users_model[:, 0]),
    "Recall@1": recall_score(users_ideal[:, 0], users_model[:, 0]),
    
    # MAP@3: сравниваем первые 3 позиции с идеалом
    "MAP@3": np.mean([
        average_precision_score(ideal[:3], model[:3]) 
        for ideal, model in zip(users_ideal, users_model)
    ]),
    
    # NDCG@3: отношение DCG текущего к DCG идеального
    "NDCG@3": np.mean([
        ndcg_score([ideal[:3]], [model[:3]], k=3)
        for ideal, model in zip(users_ideal, users_model)
    ])
}

print("Метрики для некорректного ранжирования:")
for name, val in metrics.items():
    print(f"{name}: {val:.4f}")