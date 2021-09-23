def frame():
    name = input("Enter your name and i'll frame it: ")
    dash = "-"
    side = "|"
    corner = "+"

    for y in range(len(name)+4):
        if y == 0:
            print(corner, end = "")
        print(dash, end = "")
        
    for x in corner:
        print(corner)
        print(side,"  ", name, "  ", sep = "", end = side)
        print()

    for i in range(len(name)+4):
        if i == 0:
            print(corner, end = "")
        print(dash, end = "")
    for j in corner:
        print(corner)
    
        
frame()
