#Tyler Hegewald
#Pay Raise 2
def main():
    cont = 'y'
    while cont == 'y':
        data = []
    
        data = userInput()
        first = data[0]
        last = data[1]
        oldSalary = data[2]
        salary = newSalary(float(oldSalary))
        output(first,last,salary)
        outToFile(data)
        cont = input("Do you want to enter another employee? (y/n): ")


def userInput():
    data = []
    first = input("Please enter your first name ")
    last = input("Please enter your last name ")
    oldSalary = input("Please enter your current salary ")
    data.append(first)
    data.append(last)
    data.append(oldSalary)
    return data
    


def newSalary(oldSalary):
    if oldSalary < 40000:
        newSalary = oldSalary + (oldSalary * .05)

    if oldSalary >= 40000:
        newSalary = ((oldSalary - 40000) * 1.02) + 42000
    return newSalary


def output(first,last,newSalary):
    print("First name:", format("%-10s"%first))
    print("Last name:", format("%-10s"%last))
    print("New salary:",format("$%.2f"%newSalary))

def outToFile(data):
    fw = open("data.th", 'a')
    fw.write(str(data[0]) +','+ str(data[1]) +','+ str(data[3]) +','+ str(newSalary) +'\n')
    fw.close()
    

main()
