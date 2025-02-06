import time
import Globals


seedRounds = 1
populationRounds = 2
mutationRateRounds = 3
crossoverRateRounds = 3

def SeedLoop(NextFunction, *args, **kwargs):
    global seedRounds
    for i in range(seedRounds):
        seed:int = 0
        if(Globals.saveState):
            f = open(".savestate",'r')
            content = f.readlines()
            seed = int(content[5])
        else:
            seed = int(time.time())
        NextFunction(*args, **kwargs, seed = 1728163178, seedRound = i)

def PopulationLoop(NextFunction, *args, **kwargs):
    global populationRounds
    populationSize = 1
    for i in range(populationRounds):
        populationSize *= 10
        NextFunction(*args, **kwargs, populationSize = populationSize)

def MutationRateLoop(NextFunction, *args, **kwargs):
    global mutationRateRounds
    for i in range(mutationRateRounds):
        mutationRate = 0.01 + 0.045 * i
        NextFunction(*args, **kwargs, mutationRate = round(mutationRate, 3))

def CrossoverRateLoop(NextFunction, *args, **kwargs):
    global crossoverRateRounds
    for i in range(crossoverRateRounds):
        crossoverRate = 0.1 + 0.4 * i
        NextFunction(*args, **kwargs, crossoverRate = round(crossoverRate, 3))

if __name__ == "__main__":
    SeedLoop(PopulationLoop,MutationRateLoop,CrossoverRateLoop,PrintOk)