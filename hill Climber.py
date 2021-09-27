import random

def randomSolution(population):
    pop = []
    for i in range(len(population)):
        pop.append(random.choice(population))
    return pop

def mappoints(map, mapper):
    mapped = {}
    for i in range(len(mapper)):
        for j in map.keys():
            if j == mapper[i]:
                #print(mapper[i], map.get(i))
                mapped[j] = map.get(i)
    return mapped

def fitnes(list1, list2, map):
    list3 = []
    list1, list2 = mappoints(map, list1), mappoints(map, list2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if i != j:
                fit = abs(list1[i]-list1[j]) * abs(list2[i]-list2[j])
                list3.append(fit)
    return round(min(list3),4)

def getNeighbours(currSolution):
    neighbours = []
    for i in currSolution:
        for j in range(len(i)):
            for k in range(len(i)):
                J, K = random.randint(0,len(currSolution[0])-1), random.randint(0,len(currSolution[0])-1)
                neighbour = i.copy()
                neighbour[J], neighbour[K] = neighbour[K], neighbour[J]
                neighbours.append(neighbour)
    return neighbours

def GetNeighbours(currSolution):
    neighbours = []
    for i in range(len(currSolution)):
        j,k = random.randint(0,len(currSolution)-1), random.randint(0,len(currSolution)-1)
        neighbour = currSolution.copy()
        neighbour[j], neighbour[k] = neighbour[k], neighbour[j]
        neighbours.append(neighbour)
    return neighbours

def getBestNeighbour(mapper1,neighbours, map):
    bestFitness = fitnes(mapper1, neighbours[0], map)
    bestNeighbour = neighbours[0]
    for neigh in neighbours:
        currFitness = fitnes(mapper1, neighbours[0], map)
        if currFitness > bestFitness:
            bestFitness = currFitness
            bestNeighbour = neigh
    return bestNeighbour, bestFitness

def hillclimbing(mapper1, population, map):
    currSolution = randomSolution(population)
    currFitness = fitnes(mapper1, currSolution[-1], map)
    neighbours = getNeighbours(currSolution)
    bestNeighbour, bestFitness = getBestNeighbour(mapper1, neighbours, map)
    while bestFitness <= 8.0:
            currSolution = bestNeighbour
            currFitness = bestFitness
            neighbours = GetNeighbours(currSolution)
            bestNeighbour, bestFitness = getBestNeighbour(mapper1, neighbours, map)
            print(bestNeighbour, bestFitness)

    return bestNeighbour, bestFitness

map = {
0:complex(0.4619,0.1913), 1:complex(0.1913,0.4619), 2:complex(-0.4619,0.1913),3:complex(-0.1913,0.4619),
4:complex(0.4619,-0.1913), 5:complex(0.1913,-0.4619), 6:complex(-0.4619,-0.1913), 7:complex(-0.1913,-0.4619),
8:complex(0.9239,0.3827), 9:complex(0.3827,0.9239), 10:complex(-0.9239,0.3827), 11:complex(-0.3827,0.9239),
12:complex(0.9239,-0.3827), 13:complex(0.3827,-0.9239), 14:complex(-0.9239,-0.38227), 15:complex(-0.3827,-0.9239)
}
print(map.values())
mapper = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
mapper2 = [12,10,13,9,15,11,8,14,6,5,7,3,1,4,0,2]
mapper3 = [12, 10, 8, 13, 14, 0, 3, 15, 11, 7, 6, 1, 5, 2, 4, 9]

maps = [mapper, mapper2]

print(hillclimbing(mapper, maps, map))