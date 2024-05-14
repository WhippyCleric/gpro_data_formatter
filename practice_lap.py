from car_setup import CarSetup


class PracticeLap:

    lap_number = None
    time = None
    mistake = None
    net = None
    car_setup = None

    def __init__(self, prop_list):
        self.lap_number = int(prop_list[0])
        self.time = prop_list[1]
        self.mistake = prop_list[2]
        self.net = prop_list[3]
        self.car_setup = CarSetup(prop_list[4:11])

    def __str__(self):
        return (f"Lap: {self.lap_number}\n"
                f"Time: {self.time}\n"
                f"Mistake: {self.mistake}\n"
                f"Net: {self.net}\n"
                f"{self.car_setup}")
