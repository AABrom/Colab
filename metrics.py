from rankeval import RankEval

# Жёстко заданные данные
users = [
    [1, 0, 0, 0, 0, 1],  # user1
    [0, 1, 0, 0, 0, 1],  # user2
    [0, 0, 1, 0, 0, 1],  # user3
]

# Формируем qrels: релевантности для каждого пользователя и документа
qrels = {
    f"user{i+1}": {f"doc{j+1}": rel for j, rel in enumerate(users[i])} for i in range(len(users))
}

# Ранжирование: просто doc1..doc6 для каждого пользователя
run = {
    f"user{i+1}": [f"doc{j+1}" for j in range(6)] for i in range(len(users))
}

# Создаём объект RankEval
evaluator = RankEval(
    qrels=qrels,
    cutoff=3,            # cut-off top-k (например k=3)
    relevance_method="binary"  # если у вас бинарные релевантности (0 или 1)
)

# Вычисляем метрики
results = evaluator.evaluate(run)

# Выводим результаты
for metric, score in results.items():
    print(f"{metric}@3 = {score:.4f}")
