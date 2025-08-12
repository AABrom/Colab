from pyrankeval import Rm3Evaluator

# Жёстко задаём релевантность по пользователям и докам (0/1)
# user1: doc1 - релевантен, doc2 - нет, ..., doc6 - релевантен
qrels = {
    "user1": {"doc1": 1, "doc2": 0, "doc3": 0, "doc4": 0, "doc5": 0, "doc6": 1},
    "user2": {"doc1": 0, "doc2": 1, "doc3": 0, "doc4": 0, "doc5": 0, "doc6": 1},
    "user3": {"doc1": 0, "doc2": 0, "doc3": 1, "doc4": 0, "doc5": 0, "doc6": 1},
}

# Ранжирование по пользователям: просто порядок doc1..doc6 (ранг 1..6)
run = {
    "user1": ["doc1", "doc2", "doc3", "doc4", "doc5", "doc6"],
    "user2": ["doc1", "doc2", "doc3", "doc4", "doc5", "doc6"],
    "user3": ["doc1", "doc2", "doc3", "doc4", "doc5", "doc6"],
}

# Инициализируем evaluator
evaluator = Rm3Evaluator()

# Считаем метрики с cutoff k=3
results = evaluator.evaluate(qrels, run, metrics=["map", "ndcg", "precision", "recall"], k=3)

for metric, value in results.items():
    print(f"{metric}@3 = {value:.4f}")
