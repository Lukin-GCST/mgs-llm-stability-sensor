from mgs.sensor import MGSSensor

sensor = MGSSensor()

tests = [
    "Paris is the capital of France",
    "A triangle has three sides",
    "Yesterday soup flew through time because inflation equals cosine"
]

print("TEXT | G-INDEX | STATUS")
print("-" * 40)
for t in tests:
    r = sensor.analyze(t)
    print(f"{t[:30]}... | {r['g_index']} | {r['status']}")
