num = int(input())
scores = list(input().split())
scores = [int(i) for i in scores]
max_score = max(scores)
new_scores = [(i/max_score) * 100 for i in scores]

print(f"{sum(new_scores) / num}")