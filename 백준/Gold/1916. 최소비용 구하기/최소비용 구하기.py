import sys
input = sys.stdin.readline
import heapq
n = int(input().strip())
m = int(input().strip())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    s, a, weight = map(int, input().strip().split())
    graph[s].append((a, weight))
start, arrive = map(int, input().split())
def dijkstra(scity):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        current_cost, current_city = heapq.heappop(queue)
        if current_cost > distance[current_city]:
            continue
        for next_city, travel_cost in graph[current_city]:
            total_cost = current_cost + travel_cost
            if total_cost < distance[next_city]:
                distance[next_city] = total_cost
                heapq.heappush(queue, (total_cost, next_city))
    return distance
min_cost = dijkstra(start)
print(min_cost[arrive])