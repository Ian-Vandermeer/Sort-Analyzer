# Sort Analyzer by Mr. V
import time


def main():
    # Load data files into variables
    randomData = loadDataArray("data-files/random-values.txt")
    reversedData = loadDataArray("data-files/reversed-values.txt")
    fewUniqueData = loadDataArray("data-files/few-unique-values.txt")
    nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
    
    # Test file load
    # print(randomData[0:15])
    # print(reversedData[0:15])
    # print(fewUniqueData[0:15])
    # print(nearlySortedData[0:15])

    # Main Menu
    loop = True
    while loop:
        # Print main menu and get user selection
        selection = mainMenu()

        # Process selection
        if (selection == "1"):
            print("\nBubble Sort Random Data")
            randomCopy = randomData[:]
            startTime = time.time()
            bubbleSort(randomCopy)
            endTime = time.time()
            timeToDoStuff = endTime - startTime
            print(timeToDoStuff)

        elif (selection == "2"):
            print("\nBubble Sort Reversed Data")
            reversedCopy = reversedData[:]
            startTime = time.time()
            bubbleSort(reversedCopy)
            endTime = time.time()
            timeToDoStuff = endTime - startTime
            print(timeToDoStuff)

        elif (selection == "3"):
            print("\nBubble Sort Few Unique Data")
            fewUniqueCopy = fewUniqueData[:]
            startTime = time.time()
            bubbleSort(fewUniqueCopy)
            endTime = time.time()
            timeToDoStuff = endTime - startTime
            print(timeToDoStuff)

        elif (selection == "4"):
            print("\nBubble Sort Nearly Sorted Data")
            nearlySortedCopy = nearlySortedData[:]
            startTime = time.time()
            bubbleSort(nearlySortedCopy)
            endTime = time.time()
            timeToDoStuff = endTime - startTime
            print(timeToDoStuff)

        elif (selection == "5"):
            print("\nSelection Sort Random Data")
            randomCopy = randomData[:]
            startTime = time.time()
            selectionSort(randomCopy)
            endTime = time.time()
            timeToDoStuff = endTime - startTime
            print(timeToDoStuff)

        elif (selection == "6"):
            print("\nSelection Sort Reversed Data")
            reversedCopy = reversedData[:]
            startTime = time.time()
            selectionSort(reversedCopy)
            endTime = time.time()
            timeToDoStuff = endTime - startTime
            print(timeToDoStuff)

        elif (selection == "7"):
            print("\nSelection Sort Few Unique Data")
            fewUniqueCopy = fewUniqueData[:]
            startTime = time.time()
            selectionSort(fewUniqueCopy)
            endTime = time.time()
            timeToDoStuff = endTime - startTime
            print(timeToDoStuff)

        elif (selection == "8"):
            print("\nSelection Sort Nearly Sorted Data")
            nearlySortedCopy = nearlySortedData[:]
            startTime = time.time()
            selectionSort(nearlySortedCopy)
            endTime = time.time()
            timeToDoStuff = endTime - startTime
            print(timeToDoStuff)

        elif (selection == "9"):
            print("\nInsertion Sort Random Data")
            randomCopy = randomData[:]
            startTime = time.time()
            insertionSort(randomCopy)
            endTime = time.time()
            timeToDoStuff = endTime - startTime
            print(timeToDoStuff)
            
        elif (selection == "10"):
            print("\nInsertion Sort Reversed Data")
            reversedCopy = reversedData[:]
            startTime = time.time()
            insertionSort(reversedCopy)
            endTime = time.time()
            timeToDoStuff = endTime - startTime
            print(timeToDoStuff)

        elif (selection == "11"):
            print("\nInsertion Sort Few Unique Data")
            fewUniqueCopy = fewUniqueData[:]
            startTime = time.time()
            insertionSort(fewUniqueCopy)
            endTime = time.time()
            timeToDoStuff = endTime - startTime
            print(timeToDoStuff)
            
        elif (selection == "12"):
            print("\nInsertion Sort Nearly Sorted Data")
            nearlySortedCopy = nearlySortedData[:]
            startTime = time.time()
            insertionSort(nearlySortedCopy)
            endTime = time.time()
            timeToDoStuff = endTime - startTime
            print(timeToDoStuff)
        elif (selection == "13"):
            print("\nPython Sort Random Data")
            randomCopy = randomData[:]
            startTime = time.time()
            sorted(randomCopy)
            endTime = time.time()
            timeToDoStuff = endTime - startTime
            print(timeToDoStuff)
            
        elif (selection == "14"):
            loop = False
    # end while loop
    print("goodbye")
# end main()


def loadDataArray(fileName):
    # Return data from file as an array of integers.
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp
# end loadDataArray()


def mainMenu():
    # Print Main Menu
    print("\nMain Menu")
    print("1: Bubble Sort Random Data")
    print("2: Bubble Sort Reversed Data")
    print("3: Bubble Sort Few Unique Data")
    print("4: Bubble Sort Nearly Sorted Data")
    print("5: Selection Sort Random Data")
    print("6: Selection Sort Reversed Data")
    print("7: Selection Sort Few Unique Data")
    print("8: Selection Sort Nearly Sorted Data")
    print("9: Insertion Sort Random Data")
    print("10: Insertion Sort Reversed Data")
    print("11: Insertion Sort Few Unique Data")
    print("12: Insertion Sort Nearly Sorted Data")
    print("13: Python Built in Sort Random Data")
    print("14: Exit")
    return input("Enter menu selection (1-14): ")
# end mainMenu()

def bubbleSort(anArray):
    for passnum in range(len(anArray)-1,0,-1):
        for i in range(passnum):
            if anArray[i] > anArray[i + 1]:
                temp = anArray[i]
                anArray[i] = anArray[i + 1]
                anArray[i + 1] = temp

def selectionSort(anArray):
    for fillSlot in range(len(anArray)-1):
        positionOfMin = fillSlot
        for i in range(fillSlot+1, len(anArray)):
            if anArray[i] < anArray[positionOfMin]:
                positionOfMin = i
        temp = anArray[fillSlot]
        anArray[fillSlot] = anArray[positionOfMin]
        anArray[positionOfMin] = temp

def insertionSort(anArray):
    for index in range(1, len(anArray)):
        current = anArray[index]
        position = index
 
        while position > 0 and anArray[position-1] > current:
            anArray[position] = anArray[position-1]
            position -= 1
        anArray[position] = current



# Call main() to begin program
main()
