


"""import re

zen = """ Хотя никогда зачастую лучше, чем прямо сейчас.
Если реализацию сложно объяснить - идея плоха.
Если реализацию легко объяснить - идея, возможно, хороша.
Простратсва что-то там что-то тамчто-то тамчто-то там"""

m = re.findall("^Если", zen, re.MULTILINE)


print(m)

"""
import re
l = "Красивое лучше, чем уродливое."

matches = re.findall("Красивое", l, re.IGNORECASE)

print(matches)

l1



"""import re
l = "Красивое лучше, чем уродливое."

matches = re.findall("Красивое", l)

print(matches)
"""