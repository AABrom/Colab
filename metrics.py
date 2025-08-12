from pyrankeval import Rm3Evaluator

# Пример: 3 пользователя (query_id), для каждого задан список результатов (с ранжированием) с релевантностью

qrels = {
    'user1': {'doc1': 1, 'doc2': 0, 'doc3': 0},
    'user2': {'doc1': 0, 'doc2': 1, 'doc3': 0},
    'user3': {'doc1': 0, 'doc2': 0, 'doc3': 1},
}

# Ранжированные рекомендации (doc_id и ранк)
run = {
    'user1': ['doc1', 'doc2', 'doc3'],
    'user2': ['doc2', 'doc1', 'doc3'],
    'user3': ['doc3', 'doc1', 'doc2'],
}

evaluator = Rm3Evaluator()

results = evaluator.evaluate(qrels, run, metrics=['map', 'ndcg', 'precision'], k=3)

print("Метрики ранжирования с RankEval:")
for metric in results:
    print(f"{metric}: {results[metric]}")
