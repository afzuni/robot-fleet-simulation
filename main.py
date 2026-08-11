import random


class Robot:
    def __init__(self, name, battery=100, low_battery_threshold=20):
        self.name = name
        self.battery = battery
        self.location = "Base"
        self.low_battery_threshold = low_battery_threshold

    def consume_battery(self, amount):
        self.battery -= amount
        if self.battery < 0:
            self.battery = 0

    def move(self, destination):
        print(f"{self.name} is moving to {destination}.")
        self.location = destination

    def status(self):
        print(f"{self.name} | Battery: {self.battery}% | Location: {self.location}")

    def perform_mission(self, mission):
        if self.battery < self.low_battery_threshold:
            print(f"WARNING: {self.name} battery low ({self.battery}%), returning to Base to recharge.")
            self.move("Base")
            self.battery = 100
            return False

        print(f"{self.name} started mission '{mission.title}'.")
        self.move(mission.destination)
        self.consume_battery(mission.battery_cost)
        print(f"{self.name} completed the mission successfully.")
        return True


class DroneRobot(Robot):
    def __init__(self, name, battery=100, max_altitude=50):
        super().__init__(name, battery)
        self.max_altitude = max_altitude

    def move(self, destination):
        print(f"{self.name} is flying to {destination} (altitude {self.max_altitude}m).")
        self.location = destination


class GroundRobot(Robot):
    def move(self, destination):
        print(f"{self.name} is driving to {destination} on the ground.")
        self.location = destination


class UnderwaterRobot(Robot):
    def __init__(self, name, battery=100, max_depth=30):
        super().__init__(name, battery)
        self.max_depth = max_depth

    def move(self, destination):
        print(f"{self.name} is swimming to {destination} (depth {self.max_depth}m).")
        self.location = destination


class Mission:
    def __init__(self, title, destination, battery_cost):
        self.title = title
        self.destination = destination
        self.battery_cost = battery_cost


def run_simulation():
    fleet = [
        DroneRobot("Falcon", battery=60, max_altitude=80),
        GroundRobot("Rover", battery=25),
        UnderwaterRobot("Nemo", battery=90, max_depth=40),
    ]

    missions = [
        Mission("Area Reconnaissance", "Zone-A", battery_cost=30),
        Mission("Cargo Delivery", "Zone-B", battery_cost=25),
        Mission("Environmental Monitoring", "Zone-C", battery_cost=15),
    ]

    print("=== Fleet Simulation Started ===\n")

    for robot in fleet:
        mission = random.choice(missions)
        robot.perform_mission(mission)
        robot.status()
        print("-" * 40)


if __name__ == "__main__":
    run_simulation()