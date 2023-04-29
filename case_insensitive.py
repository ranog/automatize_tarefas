"""
Para fazer sua regex ignorar as diferenças entre letras maiúsculas e
minúsculas (ser case-insensitive), re.IGNORECASE ou re.I pode ser
passado como segundo argumento de re.compile().
"""

import re

robocop = re.compile(r'robocop', re.I)

RoboCop = robocop.search('RoboCop is part man, part machine, all cop.').group()

ROBOCOP = robocop.search('ROBOCOP protects the innocent.').group()

lower_case_robocop = robocop.search('AI, why does your programming brook talks about robocop so much?').group()

print("RoboCop == " + RoboCop)
print("ROBOCOP == " + ROBOCOP)
print("robocop == " + lower_case_robocop)
