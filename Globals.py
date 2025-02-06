from pymoo.operators.sampling.rnd import IntegerRandomSampling

def initialize():
    global NUMBER_OF_PIPES
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


