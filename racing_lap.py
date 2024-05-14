import re


class RacingLap:

    lap_number = None
    time = None
    position = None
    tyre_type = None
    weather = None
    temp = None
    humidity = None
    events = None

    def __init__(self, lap_line):
        self.lap_number = lap_line[0]
        self.time = lap_line[1]
        self.position = int(lap_line[2])
        self.tyre_type = lap_line[3]
        self.weather = lap_line[4]
        self.temp = int(re.sub("\D", "", lap_line[5]))
        self.humidity = int(re.sub("\D", "", lap_line[6]))
        self.events = lap_line[7]

    def __str__(self):
        return (f"Lap: {self.lap_number}\n"
                f"Time: {self.time}\n"
                f"Position: {self.position}\n"
                f"Tyre Compound: {self.tyre_type}\n"
                f"Weather: {self.weather}\n"
                f"Temp: {self.temp}\n"
                f"Humidity: {self.humidity}\n"
                f"Events: {self.events}")
