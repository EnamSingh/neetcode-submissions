class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [] #postition, speed

        for i in range(len(position)):
            pair.append((position[i], speed[i]))

        pair.sort(reverse = True)


        fleet = 0
        slowestTime = 0

        for pos, spd in pair:
            time = (target - pos) / spd

            if time > slowestTime:
                fleet +=1
                slowestTime = time

        return fleet