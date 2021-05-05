r = Region(0,0,543,1080)
e = Region(112,825,414,191)
t = Region(442,67,97,54)
while (1):
    while t.exists("1620176331495.png"):
        count = 0
        while (count < 10): 
            if e.exists("1620175412375.png"):
                click("1620175412375.png")
            elif e.exists("1620175812567.png"):
                e.click("1620175812567.png")
            elif e.exists("1620176025055.png"):
                e.click("1620176025055.png")
            else:
                click(Location(179, 881))
            count = count + 1
            if (count % 2 == 0): 
                click(Location(295, 767))
            else:
                click(Location(256, 780))
        if exists("1559495990919.png"):
            click("1559495997663.png")
    if exists("1620173932825.png"):
        click("1620173948169.png")
    elif exists("1620174184224.png"):
            click("1620174189673.png")
            
    elif exists("1559494554041.png"):
        click("1559494562164.png")
    elif exists("1559495990919.png"):
        click("1559495997663.png")