from mgs.sensor import MGSSensor

sensor = MGSSensor()

text = "Complex systems self-organize toward stable attractors"
result = sensor.analyze(text)
print(result)
