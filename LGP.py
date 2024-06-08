from pkg_resources import resource_filename
from Warriors import Warrior as warrior
from Config import config

import re
import os

import numpy as np
import transformations as transform
import matplotlib.pyplot as plt


# INDEX:
# init_population(): initializes 10 programs
# load_warriors(): writes program instruction to the files in exhaust_ma
# test_program(): executes command to test each programs and get those who die vs those who win
# fetch_result(): parses the result file and gets those who die and those who are alive
# grade_warrior(): assigns +1 or -5
# mutate():
DEBUG = config.DEBUG
class LGP:
    def __init__(self):
        self.population = list(self.init_population())
        self.generations = 0
        self.best_score = []
        self.worst_scores = []

        

    def run(self) -> None:
        while(self.generations < config.DESIRED_RUNS):
            print(f'Generation {self.generations}')
            self.load_warriors()
            self.test_programs()
            self.fetch_results("training")
            self.population.sort(key = warrior.sort_by_fitness, reverse = True)
            self.eliminate()
            self.crossover()
            self.mutate()
            self.gather_analytics()
            self.generations += 1

    # Initializes population
    def init_population(self) -> list:
        warriors = np.empty(config.POPULATION_SIZE, dtype=warrior)

        for i in range(config.POPULATION_SIZE):
            warriors[i] = warrior()
        return warriors
    
    # Write warriors to the files in exhaust_ma
    def load_warriors(self) -> None:
        length = len(self.population)

        # Write each program in the target file in the exhaust folder
        for i in range(length):
            f = open(f"C:/Python311/Lib/site-packages/exhaust_ma/exhaust-ma/GP/test/program{i}.rc", "w")
            for j in self.population[i].instructions:
                f.write(j)
            f.close()
        
    # Executes the program 
    def test_programs(self) -> None:
        os.system("C:/Python311/python.exe c:/Python311/Lib/site-packages/exhaust_ma/warriors_test.py")
    
    # Gets result from result .txt created
    def fetch_results(self, string: str):
        f = open(f"c:/Python311/Lib/site-packages/exhaust_ma/exhaust-ma/GP/results/{string}.txt", "r")
        lines = f.readline()

        self.dead = [int(match.group(1)) for match in re.finditer(r"'program(\d+)\.rc'", re.search(r'dead=\[(.*?)\]', lines).group(1))]
        self.alive = [int(match.group(1)) for match in re.finditer(r"'program(\d+)\.rc'", re.search(r'alive=\{(.*?)\}', lines).group(1))]

        self.grade_warriors()

        if DEBUG == 1:
            print(lines)
            print('dead:', self.dead)
            print('alive: ', self.alive)

    # Grade warriors
    def grade_warriors(self):
        length = len(self.alive)
        if(length == config.POPULATION_SIZE):
            for i in range(length):
                self.population[i].grade(config.DEATH + config.FORGIVENESS)
            return
        for i in range(length):
            self.population[self.alive[i]].grade(config.PRIZE/length)
        
        length = len(self.dead)
        for i in range(length):
            self.population[self.dead[i]].grade(-1)

    # Performs single point crossover
    def crossover(self):
        
        percentage = int(config.BEST_PERCENTAGE*config.POPULATION_SIZE)
        
        for i in range(percentage, config.POPULATION_SIZE):
            right = self.population[np.random.randint(0, percentage)].instructions
            r = np.random.randint(0, len(right))
            
            left = self.population[np.random.randint(0, percentage)].instructions
            l = np.random.randint(0, len(left))

            self.population[i].instructions = right[:r] + left[l:]
        
            self.check_length(self.population[i])

    def mutate(self):
        percentage = int(config.BEST_PERCENTAGE*config.POPULATION_SIZE)
        
        for i in range(percentage, config.POPULATION_SIZE):
            if(np.random.uniform(0, 1) <= config.MUTATION_RATE):
                transform.change_operation(self.population[i])
            if(np.random.uniform(0, 1) <= config.MUTATION_RATE/2):
                transform.change_address_modifier(self.population[i])
            if(np.random.uniform(0, 1) <= config.MUTATION_RATE/2):
                transform.change_instruction_modifer(self.population[i])
            if(np.random.uniform(0, 1) <= config.MUTATION_RATE/len(self.population[i].instructions)):
                transform.change_sources(self.population[i])

    def eliminate(self):
        length = len(self.population)
        for i in range(length):
            if(self.population[i].score <= config.DEATH):
                self.population[i].restart()
    
    def check_length(self, w: warrior):
        if(len(w.instructions) > config.MAX_INSTRUCTIONS):
            w.instructions = w.instructions[0:config.MAX_INSTRUCTIONS]

    def gather_analytics(self):
        self.best_score += [self.population[0].score]
        self.worst_scores += [self.population[config.POPULATION_SIZE-1].score]

    def print_analytics(self, id: int):
        print(" ----------- Best program: ----------------")
        self.population[0].print_information()
        x = np.arange(0, self.generations)
        y = self.best_score
        z = self.worst_scores

        plt.plot(x, y, color="green", label= 'Best scores')
        plt.plot(x, z, color="red", label = 'Worst scores')

        plt.legend()
        plt.xlabel("generations")
        plt.ylabel("scores")
        plt.title(f'Run {id}: scores per generations')
        
        plt.savefig(f'run{id}.png')
        plt.clf()
        plt.cla()

    def write_analytics(self, file: str):
        f = open(file, "w")
        [f.write(f'{self.best_score[i]}\n') for i in range(self.generations)]
        f.close()
    
    def write_champion_warrior(self, id: int):
        f = open(f'champions/{self.population[0].name}_run{id}', "w")
        f.write(f';score {self.population[0].score}\n')
        [f.write(f'{self.population[0].instructions[i]}\n') for i in range(len(self.population[0].instructions))]
