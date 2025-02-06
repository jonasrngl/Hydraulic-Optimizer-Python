from CustomEpanet import epanet
import os
import gc

# from main import mutex
   
def ObjectiveFunction(splitDpInput):
    
    diameter_pattern=[]
    
    for i in range(len(splitDpInput)):
        diameter_pattern.append(int(splitDpInput[i]))

    total_cost:int = 0
    sum_RI: float = 0.0
    A: float = 0.0
    B: float = 0.0
    Hmin: float = 30.0

    # Loading Network
    d = epanet('./app/EPANET/Alperovits_Shamir.inp', loadfile=True, verbose=False, multithreading=False)

    d.openHydraulicAnalysis()
    d.initializeHydraulicAnalysis(0)

    Nlinks = d.getLinkCount()
    Nnodes = d.getNodeCount()
    Nres_tanks = d.getNodeTankReservoirCount()
    Njunctions = Nnodes - Nres_tanks

    diameter = []
    pipe_cost = []

    finput = open('./app/Tabela_Custos.txt', 'rt')

    number_diameters = int(finput.readline().split()[0])

    diameter_base = []
    cost_base = []

    next(finput)

    for line in finput:
        current = line.split()
        obs1 = current[0]
        obs2 = current[1]
        obs3 = current[2]

        diameter_base.append(float(obs2))
        cost_base.append(float(obs3))

    finput.close()

    for i in range(Nlinks):
        aux = diameter_pattern[i]
        diameter.append(diameter_base[aux])
        d.setLinkDiameter(i + 1, diameter[i])
        pipe_length = d.getLinkLength(i + 1)

        pipe_cost.append(cost_base[aux] * pipe_length)
        total_cost += pipe_cost[i]
        

    # Hydraulic Analysis

    # mutex.acquire()

    t = d.runHydraulicAnalysis()

    # mutex.release()

    # Warning6 = False

    for i in range(Njunctions):

        # junction_pressure = d.getNodePressure(i + Nres_tanks)
        junction_pressure = d.api.ENgetnodevalue(i + Nres_tanks, d.ToolkitConstants.EN_PRESSURE)

        if (junction_pressure < Hmin):
            # Warning6 = True
            total_cost += (Hmin - junction_pressure) * 10000000.0
            sum_RI -= (Hmin - junction_pressure) * 100.0
            # break
        else:
            # junction_demand = d.api.ENgetnodevalue(i + Nres_tanks, d.ToolkitConstants.EN_DEMAND)
            junction_demand = d.getNodeActualDemand(i + Nres_tanks)
            aux1 = junction_demand * (junction_pressure - Hmin)
            A += aux1
            aux2 = junction_demand * Hmin
            B += aux2

    if(B != 0):
        sum_RI += 100 * (A / B)

    d.closeHydraulicAnalysis()

    #d.saveHydraulicsOutputReportingFile()

    #d.setReportFormatReset()
    #d.setReport('FILE Output.rpt')
    #d.setReport('STATUS YES')
    #d.setReport('SUMMARY YES')
    #d.setReport('MESSAGES YES')
    #d.writeReport()

    d.unload()

    del d

    print(f"{total_cost} {(-1)*sum_RI}")
#--------------------------------------------------

if __name__ == '__main__':
    ObjectiveFunction()