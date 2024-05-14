class CarSetup:

    front_wing = None
    rear_wing = None
    engine = None
    brakes = None
    gear = None
    suspension = None
    tyre_type = None

    def __init__(self, setup_list):
        self.front_wing = int(setup_list[0])
        self.rear_wing = int(setup_list[1])
        self.engine = int(setup_list[2])
        self.brakes = int(setup_list[3])
        self.gear = int(setup_list[4])
        self.suspension = int(setup_list[5])
        self.tyre_type = setup_list[6]

    def __str__(self):
        return (f"Front Wing: {self.front_wing}\n"
                f"Rear Wing: {self.rear_wing}\n"
                f"Engine: {self.engine}\n"
                f"Brakes: {self.brakes}\n"
                f"Gears: {self.gear}\n"
                f"Suspension: {self.suspension}\n"
                f"Tyre Compound: {self.tyre_type}")
