import math

class ProjectileMotion:
    def __init__(self):
        self.initial_velocities = []
        self.launch_angles = []
        self.time_of_flights = []

    def add_launch_parameters(self, v, angle):
        
        self.initial_velocities.append(v)

        self.launch_angles.append(angle)

    def get_initial_velocities(self):
        return self.initial_velocities
    
    def get_launch_angles(self):
        return self.launch_angles

    def get_time_of_flights(self):
        for v, angle in zip(self.initial_velocities, self.launch_angles):
            self.time_of_flight = (2 * v * math.sin(math.radians(angle)))/9.81
            self.time_of_flights.append(self.time_of_flight)
        return self.time_of_flights

    def get_flight_ranges(self):
        flight_ranges = []
        for v, angle in zip(self.initial_velocities, self.launch_angles):
            time_of_flight = (2 * v * math.sin(math.radians(angle)))/9.81

            flight_range = time_of_flight * v * math.cos(math.radians(angle))
            flight_ranges.append(flight_range)

        return flight_ranges

speedy = ProjectileMotion()
speedy.add_launch_parameters(v=28, angle=68)
speedy.add_launch_parameters(v=11, angle=15)

v = speedy.get_initial_velocities()
angles = speedy.get_launch_angles()
x = speedy.get_flight_ranges()
t = speedy.get_time_of_flights()

print(f"{v=}")
print(f"{angles=}")
print(f"{x=}")
print(f"{t=}")