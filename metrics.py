import rankeval

# Жёстко задаём релевантности (qrels)
qrels = {
    "user1": {"doc1": 1, "doc2": 0, "doc3": 0, "doc4": 0, "doc5": 0, "doc6": 1},
    "user2": {"doc1": 0, "doc2": 1, "doc3": 0, "doc4": 0, "doc5": 0, "doc6": 1},
    "user3": {"doc1": 0, "doc2": 0, "doc3": 1, "doc4": 0, "doc5": 0, "doc6": 1},
}

# Жёстко задаём run (ранжирование)
run = {
    "user1": ["doc1", "doc2", "doc3", "doc4", "doc5", "doc6"],
    "user2": ["doc1", "doc2", "doc3", "doc4", "doc5", "doc6"],
    "user3": ["doc1", "doc2", "doc3", "doc4", "doc5", "doc6"],
}

# Создаём объект метрик с cutoff=3
metrics = rankeval.metrics.create(metrics=["map", "ndcg", "precision", "recall"], cutoff=3)

# Запускаем вычисление
results = rankeval.evaluate(qrels, run, metrics=metrics)

# Выводим результаты
for metric_name, score in results.items():
    print(f"{metric_name}@3 = {score:.4f}")
