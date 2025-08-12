import ir_measures
from ir_measures import Qrel, Result, map, ndcg, precision, recall

# Жёстко задаём релевантность (qrels)
qrels = [
    Qrel("user1", "doc1", 1), Qrel("user1", "doc2", 0), Qrel("user1", "doc3", 0),
    Qrel("user1", "doc4", 0), Qrel("user1", "doc5", 0), Qrel("user1", "doc6", 1),

    Qrel("user2", "doc1", 0), Qrel("user2", "doc2", 1), Qrel("user2", "doc3", 0),
    Qrel("user2", "doc4", 0), Qrel("user2", "doc5", 0), Qrel("user2", "doc6", 1),

    Qrel("user3", "doc1", 0), Qrel("user3", "doc2", 0), Qrel("user3", "doc3", 1),
    Qrel("user3", "doc4", 0), Qrel("user3", "doc5", 0), Qrel("user3", "doc6", 1),
]

# Жёстко задаём ранжирование рекомендаций (run) — просто doc1..doc6 в этом порядке для всех пользователей
run = [
    Result("user1", "doc1", rank=1, score=1.0), Result("user1", "doc2", rank=2, score=0.9),
    Result("user1", "doc3", rank=3, score=0.8), Result("user1", "doc4", rank=4, score=0.7),
    Result("user1", "doc5", rank=5, score=0.6), Result("user1", "doc6", rank=6, score=0.5),

    Result("user2", "doc1", rank=1, score=1.0), Result("user2", "doc2", rank=2, score=0.9),
    Result("user2", "doc3", rank=3, score=0.8), Result("user2", "doc4", rank=4, score=0.7),
    Result("user2", "doc5", rank=5, score=0.6), Result("user2", "doc6", rank=6, score=0.5),

    Result("user3", "doc1", rank=1, score=1.0), Result("user3", "doc2", rank=2, score=0.9),
    Result("user3", "doc3", rank=3, score=0.8), Result("user3", "doc4", rank=4, score=0.7),
    Result("user3", "doc5", rank=5, score=0.6), Result("user3", "doc6", rank=6, score=0.5),
]

# Список метрик, которые хотим посчитать на cutoff k=3
metrics = [map@3, ndcg@3, precision@3, recall@3]

# Запускаем агрегированные вычисления
results = list(ir_measures.calc_aggregate(metrics, qrels, run))

# Выводим результаты
for r in results:
    print(f"{r.metric}@{r.k} = {r.value:.4f}")
