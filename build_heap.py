def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)

    for i in range (n, -1, -1):
        j = i
        while True:
            z = (j * 2) + 1
            if z >= n:
                break
            if z+1 < n and data[z+1] < data[z]:
                z = z+1
            if data[j] > data[z]:
                swaps.append((j, z))
                data[j], data[z] = data[z], data[j]
                j = z
            else:
                break
    return swaps

def main():
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    # input from keyboard
    
    text = input("I or F: ")
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
    
    elif "F" in text:
        f = input()
        if "a" not in f:
            with open("tests/" + f, 'r', encoding='utf-8') as x:
                n = int(x.readline())
                data = list(map(int, x.readline().split()))
    else:
        print("Error")
        return 
    
    # checks if lenght of data is the same as the said lenght
    assert data is not None and len(data) == n
    
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)
    
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= n*4
    
    # output all swaps
    print(len(swaps))
    
    for i, j in swaps:
        print(i, j)
       
if name == "main":
    main()
