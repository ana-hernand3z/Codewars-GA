import Redcode as redcode
from Warriors import Warrior as warrior

from LGP import LGP
import numpy as np

f = open("Best_Scores", "w")
for i in range (10):
    program = LGP()
    program.run()                
    program.write_analytics(f"run{i}")
    f.write(f'{i},{program.population[0].score}\n')
    program.write_champion_warrior(i)
    program.print_analytics(i)
f.close()


