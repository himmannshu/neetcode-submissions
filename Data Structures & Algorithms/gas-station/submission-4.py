class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [(gas[i] - cost[i]) for i in range(n)]

        if sum(diff) < 0:
            return -1

        def isReachable(i, total_gas, num_stations):
            #print(f'num stations {num_stations}')
            if num_stations == n:
                return True
            #print(f'i = {i%n}, total_gas = {total_gas}')
            if total_gas < cost[i%n]:
                #print('broke')
                return False
            
            return isReachable(i + 1, total_gas - cost[i%n] + gas[(i + 1)%n], num_stations + 1)
        
        for i in range(n):
            if gas[i] >= cost[i] and isReachable(i, gas[i], 1):
                return i
        

