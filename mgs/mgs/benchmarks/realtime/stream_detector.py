from mgs.sensor import MGSSensor

class MGSRealtimeDetector:
    def __init__(self):
        self.sensor = MGSSensor()
        self.buffer = ""

    def update(self, token):
        self.buffer += token
        result = self.sensor.analyze(self.buffer)
        return result
