import sys
input = sys.stdin.readline
import heapq
n, k = map(int, input().strip().split())
def dijkstra(n,k):
    max = 100001
    dist = [float('inf')] * max
    dist[n] = 0
    queue = []
    heapq.heappush(queue,(0,n))
    while queue:
        time, curr = heapq.heappop(queue)
        if dist[curr] < time:
            continue
        move = curr * 2
        if 0 <= move < max and time < dist[move]:
            dist[move] = time
            heapq.heappush(queue, (time, move))
        move = curr -1
        if 0 <= move < max and time + 1 < dist[move]:
            dist[move] = time + 1
            heapq.heappush(queue, (time + 1, move))
        move = curr +1
        if 0 <= move < max and time + 1 < dist[move]:
            dist[move] = time + 1
            heapq.heappush(queue, (time + 1, move))
    return dist[k]
print(dijkstra(n,k))