from main import convert as convert0
from dop1 import convert as convert1
from dop2 import convert as convert2
from dop3 import convert as convert3
import timeit

text = lambda name: f"""
from __main__ import convert{name}
file = open("schedule.yaml", "r", encoding="utf-8")
convert{name}(file)
"""

for i in range(4):
    time = timeit.timeit(text(i), number=100)
    print("Execution time:", time)