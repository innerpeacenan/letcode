#如果总的加油量>=消耗肯定是可以走完一圈的，如果mygas<0说明前一站到当前站行不通，只能把起始站设为下一站
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        
        n=len(gas)
        total=0#总油量
        mygas=0#汽车的当前油量
        gas_station=0#起始加油站
        for i in range(n):
            total+=gas[i]-cost[i]
            mygas+=gas[i]-cost[i]
            if mygas<0:#若mygas为负，则将mygas置零，起始位置为当前位置的下一个车站
                mygas=0
                gas_station=i+1
        if total>=0:
            return gas_station
        else:
            return -1
                
            
           
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """