class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            x, y = points[i]
            distance = x * x + y * y

            if len(heap) < k:
                heapq.heappush(heap,(-distance, i))
            else:
                if distance < -heap[0][0]:
                    heapq.heappushpop(heap,(-distance,i))

        res = []

        for p in heap:
            index = p[1]
            res.append(points[index])
        return res