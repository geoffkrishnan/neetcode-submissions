"""
input:
    int - target
    int array - position
        position[i] - ith car
    int array - speed
        speed[i] - ith car
output:
    number of diff car fleets that arrive at target destination

car A  can't pass another car B ahead of it

can only catch up to another car and drive at same speed as faster car

car fleet - non-empty set of cars driving at same pos and speed
    single car counts as a car fleet

if car catches up to fleet at target, it counts as part of that fleet

(speed * time) + starting_pos = target_pos

time = (target_pos - starting_pos) // speed

if time of cars are the same, then they are the same fleet?

oh.

so when there's a slower car at starting position ahead of a faster car, that faster car after catching up to the slower car, then moves at the slower car's speed.


so need a way to keep track of faster cars combining with slower cars

so maybe sort by positions descending


"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 1
        curr_fleet_time = (target - cars[0][0]) / cars[0][1]
        for i in range(1, len(cars)):
            p, s = cars[i]
            if ((target - p) / s) > curr_fleet_time:
                fleets += 1
                curr_fleet_time = (target - p) / s
        return fleets
                
                


        