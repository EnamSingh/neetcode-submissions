class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [] # postition, speed

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))

        pairs.sort(reverse = True)

        fleet = 0
        slowestTime = 0

        for pos, spd in pairs:
            time = ( target - pos) / spd

            if time > slowestTime:
                fleet += 1
                slowestTime = time

        return fleet