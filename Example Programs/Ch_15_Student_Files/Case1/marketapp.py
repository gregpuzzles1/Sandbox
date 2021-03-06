from model import MarketModel

def main():
    print "Welcome to the Martket Simulator!"
    lengthOfSimulation = input("Enter the total running time: ")
    averageTimePerCus = input("Enter the average time per customer: ")
    probabilityOfNewArrival = input("Enter the probability of a new arrival: ")
    if lengthOfSimulation < 1 or lengthOfSimulation > 1000:
        print "Running time must be an integer greater than 0" + \
              "\nand less than or equal to 1000"
    elif averageTimePerCus <= 0 or averageTimePerCus >= lengthOfSimulation:
        print "Average time per customer must be an integer" + \
              "\ngreater than 0 and less than running time"
    elif probabilityOfNewArrival <= 0 or probabilityOfNewArrival > 1:
        print "Probability must be geater than 0" + \
              "\nand less than or equal to 1"
    else:
        model = MarketModel(lengthOfSimulation, averageTimePerCus,
                            probabilityOfNewArrival) 
        print model.runSimulation()

main()

   
