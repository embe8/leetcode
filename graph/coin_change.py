# Problem: given a list of integers representing value of coins and a target integer representing a specific amount,
# Find the least amount of coins needed that will add up to target
# Approach: Use BFS to get minimum path to target where nodes are the coins, return -1 when target is not reachable

class Solution:
  def coinChange(self, list: List[int], target:int)->int:
    if target == 0: return 0
    q = deque([0])
    visited = [False] * (target + 1) # max number of coins
    visited[0] = True
    numCoins = 0

    while q:
      numCoins += 1 # finished processing one coin
      for _ in range (len(q)):
        current = q.popleft()
        for coin in list:
          next = current + coin
          if next == target: return numCoins # return current coin number
          if next > target or visited[next]:
            continue
          visited[next] = True
          q.append(next)

    return -1


