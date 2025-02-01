class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_total = 0  
        
        tank = 0
        start_station = 0

        for i in range(len(gas)):
            gas_total += gas[i]-cost[i]
            
            
            tank+= gas[i] - cost[i]

            if tank<0:
                start_station = i+1
                tank = 0

        if gas_total < 0:
            return -1
        else: 
            return start_station



           

        
        

             
