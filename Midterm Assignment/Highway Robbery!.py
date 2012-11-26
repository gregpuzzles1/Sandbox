#Highway Robbery Midterm
#Example
def main():
    getData()
def getData():
    Name =         input("Please enter the customer's name..............:")
    Age =      int(input("Please enter the customer's age...............:"))
    Violations=int(input("Please enter the number of traffic violations.:"))
    calc(Name, Age, Violations)
def calc(customerName, customerAge, trafficViolations):
    if customerAge < 25:
        code = 1
        price = 480
    elif trafficViolations >=3 and trafficViolations <4:
        code = 2
        price = 450
    elif trafficViolations >=2 and trafficViolations <3:
        code = 2
        price = 405
    elif trafficViolations >=1 and trafficViolations <2:
        code = 3
        price = 380
    elif trafficViolations <1:
        code = 4
        price = 325
    elif customerAge>=25:
        if trafficViolations >=4:
            code = 1
            price = 410
        elif trafficViolations >=3 and trafficViolations <4:
            code = 2
            price = 390
        elif trafficViolations >=2 and trafficViolations <3:
            code = 2
            price = 365
        elif trafficViolations >=1 and trafficViolations <2:
            code = 3
            price = 315
        elif trafficViolations <1:
            code = 4
            price = 275

    if code ==4:
        rcode = "no"
    elif code ==3:
        rcode = "low"
    elif code ==2:
        rcode = "moderate"
    else:
        rcode = "high"
    output(customerName, rcode, price)
def output(custName, riskCode, costofIns):
    print(custName, 'as a ',riskCode, 'risk driver, your insurance will cost $',\
          format(costofIns, '.2f'))

main()
