# from threading import Lock
from threading import Semaphore
from pymoo.operators.sampling.rnd import IntegerRandomSampling

# lock = Lock()

counterSemaphore = Semaphore(1)

def initialize():
    global NUMBER_OF_PIPES
    global threadState
    global dockers
    global numberOfThreads
    global availablePorts
    global client
    global saveState
    global AVAILABLE_DIAMETERS
    global n_objectives
    global n_dimensions
    global sampling
    global generations
    global stop_criteria

    AVAILABLE_DIAMETERS = 14

    NUMBER_OF_PIPES = 8
    generations = 1000
    stop_criteria = ('n_gen', generations)

    sampling = IntegerRandomSampling()

    n_objectives = 2
    n_dimensions = n_objectives

    saveState = False
    threadState = {}
    dockers = {}
    availablePorts = []
    currentPort = 0
    numberOfThreads = 4
    for i in range(numberOfThreads * 2):
        availablePorts.append(8000 + i)


