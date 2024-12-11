#Here we define an alternative function to .sort(), passing a list as an argument
def sorted_fun(list):
    #first we define arr as a local copy of the list provided
    arr =  list.copy()
    #then we define a second empty array
    arr2 = []
    #loop start
    while True:
        #the program should find the minimum int in the array
        x = max(arr)
        #add that number to the empty list
        arr2.append(x)
        #remove the number from the copy list
        arr.remove(x)
        #if the copy array results empty the program should stop the loop
        if arr == []:
            break
    #and return the final ordered array
    return arr2


def main():
    #Creating an empty list
    arr = []

    #initiating the while loop with the condition of 0 not being present in the array
    while True:
        #looping the request for an input
        num = int(input("What value? "))
        #condition for which if the input is equal to 0, the loop should stop
        if num == 0:
            break
        #and add all the numbers provided to the array
        arr.append(num)

    #the program should iterate through every instance in the result of the sort function and print it in a new line
    for i in sorted_fun(arr):
        print(i)


if __name__ == '__main__':
    main()
