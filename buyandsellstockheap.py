import heapq as hp

def solve(arr):
    heap = []
    profit = 0

    for price in arr:
        hp.heappush(heap, price)

        if price > heap[0]:
            profit += price - hp.heappop(heap)
            hp.heappush(heap, price)

    return profit

print(solve([1,2,3,4,6,8,9]))