class QualyData:

    time = None
    risk = None
    setup = None

    def __init__(self, time, risk, setup):
        self.time = time
        self.risk = risk
        self.setup = setup

    def __str__(self):
        return (f"Time: {self.time}\n"
                f"Risk: {self.risk}\n"
                f"{self.setup}")
