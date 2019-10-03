import random

state_space = [
        [["Empty", False,1],["Treasure0",False,3],1],
        [["Empty", False,1],["Treasure1",False,3],1],
        [["Treasure0", False,3],["Light",False,3],1],
        [["Treasure1", False,3],["Light",False,3],2],
        [["Light", False,3],["Treasure1",False,3],2],
        [["Light", False,3],["Empty",False,1],1]
        ]

def expandAndReturnChildren(state_space, path_to_leaf_node):
    children = []
    for [[p,q,r],[s,t,u],c] in state_space:
        if p == path_to_leaf_node[-1]:
            children.append(path_to_leaf_node + [s])
    return children

def newExpandAndReturnChildrend(state_space, path_to_leaf_node):
    children = []
    for [[p,q,r],[s,t,u],c] in state_space:
        if p == path_to_leaf_node[-1]:
            children.append(path_to_leaf_node + [s])        
    return children

def actionCost(path, state_space, initial_state):
    cost = []
    col = 0
    totalcost = []
    count = 0
    
    while count < len(path):
        t0 = path.count("Treasure0")
        t1 = path.count("Treasure1")
        l = path.count("Light")
        t0counter = 1
        t1counter = 1
        lightcounter = 1
        cost = []
        if path[count] == "Empty":
            cost.append(1)
        elif path[count] == "Treasure0":
            if t0 == 1:
                for [x,y] in initial_state:
                    if x == path[count] and y == True:
                        cost.append(4)
                    elif x == path[count] and y == False:
                        cost.append(1)
            else:
                if t0counter == 1:
                    for [x,y] in initial_state:
                        if x == path[count] and y == True:
                            cost.append(4)
                        elif x == path[count] and y == False:
                            cost.append(1)
                    t0counter += 1
                elif t0counter > 1:
                    cost.append(1)

        elif path[count] ==  "Treasure1":
            if t1 == 1:
                for [x,y] in initial_state:
                    if x == path[count] and y == True:
                        if path[count-1] == "Light":
                            cost.append(5)
                        elif x == path[count-1] == "Empty":
                            cost.append(3)
                    elif x == path[count] and y == False:
                        if path[col][count-1] == "Light":
                            cost.append(2)
                        elif x == path[count-1] == "Empty":
                            cost.append(1)
            else:
                if t1counter == 1:
                    for [x,y] in initial_state:
                        if x == path[count] and y == True:
                            if path[count-1] == "Light":
                                cost.append(5)
                            elif x == path[count-1] == "Empty":
                                cost.append(3)
                        elif x == path[count] and y == False:
                            if path[count-1] == "Light":
                                cost.append(2)
                            elif x == path[count-1] == "Empty":
                                cost.append(1)
                    t1counter += 1
                elif t1counter > 1:
                    if path[count-1] == "Light":
                        cost.append(2)
                    elif path[count-1] == "Empty":
                        cost.append(1)

        elif path[count] == "Light":
            if l == 1:
                for [f,g] in initial_state:
                    if f == path[count] and g == True:
                        if path[count-1] == "Treasure1":
                            cost.append(2)
                        elif path[count-1] == "Treasure0":
                            cost.append(1)
                    elif f == path[count] and g == False:
                        if path[count-1] == "Treasure1":
                            cost.append(5)
                        elif path[count-1] == "Treasure0":
                            cost.append(4)
            else:
                if lightcounter == 1:
                    for [f,g] in initial_state:
                        if f == path[count] and g == True:
                            if path[count-1] == "Treasure1":
                                cost.append(2)
                            elif path[count-1] == "Treasure0":
                                cost.append(1)
                        elif f == path[count] and g == False:
                            if path[count-1] == "Treasure1":
                                cost.append(5)
                            elif path[count-1] == "Treasure0":
                                cost.append(4)
                    lightcounter += 1
                elif lightcounter > 1:
                    if path[count-1] == "Treasure1":
                        cost.append(2)
                    elif path[count-1] == "Treasure0":
                        cost.append(1)
        count += 1
        c = cost
        totalcost = c
    return totalcost



def sortSecond(val):
    return val[1]

def sortFrontier(children, state_space):
    counter = 0
    var = []
    temp = None
    newvar = []
    z = 0
    
    while counter < len(children):
        ac = actionCost(children[counter], state_space, initial_state)
        for [[p,q,r],[s,t,u],c] in state_space:
            if p == children[counter][-1]:
                var.append([children[counter],ac])
                break
        counter += 1
    print('befre',var)
    i = 0
    if len(var) > 1:
        while i < len(var):
            j = 0
            while j < len(var[i]):
                if var[i][1] <= var[j][1]:
                    temp = var[i]
                    var[i] = var[j]
                    var[j] = temp
                j += 1
            i += 1
    print('after',var)
    while z < len(var):
        y = 0
        while y < len(var[z]):
            y+=1
        newvar.append(var[z][0])
        z += 1

    return newvar


def pathAndAction(path,initial_state):
    i = 0
    t0 = path.count("Treasure0")
    t1 = path.count("Treasure1")
    l = path.count("Light")
    t0counter = 1
    t1counter = 1
    lightcounter = 1
    action = []
    
    while i < len(path):
        j = 0
        while j < len(path[i]):
            if j == 0:
                if path[i][j] == "Treasure0":
                    for [m,n] in initial_state:
                        if m == "Treasure0" and n == True:
                            action.append('grab')
                        elif m == "Treasure0" and n == False:
                            continue
                elif path[i][j] == "Treasure1":
                    for [m,n] in initial_state:
                        if m == "Treasure0" and n == True:
                            action.append('grab')
                        elif m == "Treasure1" and n == False:
                            continue
                elif path[i][j] == "Light":
                    for [m,n] in initial_state:
                        if m == "Light" and n == True:
                            continue
                        elif m == "Light" and n == False:
                            action.append('switch')
            else:
                if path[i][j] == "Empty" and path[i][j-1] == "Light":
                    action.append('down')
                elif path[i][j] == "Treasure0":
                    if path[i][j-1] == "Empty" and t0 == 1:
                        action.append('left')
                        for [m,n] in initial_state:
                            if m == "Treasure0" and n == True:
                                action.append('grab')
                            elif m == "Treasure0" and n == False:
                                continue
                    elif path[i][j-1] == "Empty" and t0counter == 1:
                        action.append('left')
                        for [m,n] in initial_state:
                            if m == "Treasure0" and n == True:
                                action.append('grab')
                            elif m == "Treasure0" and n == False:
                                continue
                        t0counter += 1
                    elif path[i][j-1] == "Empty" and t0counter > 1:
                        action.append('left')
                        for [m,n] in initial_state:
                            if m == "Treasure0" and n == True:
                                continue
                            elif m == "Treasure0" and n == False:
                                continue
                elif path[i][j] == "Light" and path[i][j-1] == "Treasure0":
                    if path[i][j-1] == "Treasure0" and l == 1:
                        action.append('upRight')
                        for [m,n] in initial_state:
                            if m == "Light" and n == True:
                                continue
                            elif m == "Light" and n == False:
                                action.append('switch')
                    elif path[i][j-1] == "Treasure0" and lightcounter == 1:
                        action.append('upRight')
                        for [m,n] in initial_state:
                            if m == "Light" and n == True:
                                continue
                            elif m == "Light" and n == False:
                                action.append('switch')
                        lightcounter += 1
                    elif path[i][j-1] == "Treasure0" and lightcounter > 1:
                        action.append('upLeft')
                        for [m,n] in initial_state:
                            if m == "Light" and n == True:
                                continue
                            elif m == "Light" and n == False:
                                continue
                elif path[i][j] == "Light" and path[i][j-1] == "Treasure1":
                    if path[i][j-1] == "Treasure1" and l == 1:
                        action.append('upLeft')
                        for [m,n] in initial_state:
                            if m == "Light" and n == True:
                                continue
                            elif m == "Light" and n == False:
                                action.append('switch')
                    elif path[i][j-1] == "Treasure1" and lightcounter == 1:
                        action.append('upLeft')
                        for [m,n] in initial_state:
                            if m == "Light" and n == True:
                                continue
                            elif m == "Light" and n == False:
                                action.append('switch')
                        lightcounter += 1
                    elif path[i][j-1] == "Treasure1" and lightcounter > 1:
                        action.append('upLeft')
                        for [m,n] in initial_state:
                            if m == "Light" and n == True:
                                continue
                            elif m == "Light" and n == False:
                                continue
                elif path[i][j] == "Treasure1" and path[i][j-1] == "Light":
                    if path[i][j-1] == "Light" and t1 == 1:
                        action.append('rightdown')
                        for [m,n] in initial_state:
                            if m == "Treasure1" and n == True:
                                action.append('grab')
                            elif m == "Treasure1" and n == False:
                                continue
                    elif path[i][j-1] == "Light" and t1counter == 1:
                        action.append('rightdown')
                        for [m,n] in initial_state:
                            if m == "Treasure1" and n == True:
                                action.append('grab')
                            elif m == "Treasure1" and n == False:
                                continue
                        t1counter += 1
                    elif path[i][j-1] == "Light" and t1counter > 1:
                        action.append('rightdown')
                        for [m,n] in initial_state:
                            if m == "Treasure0" and n == True:
                                continue
                            elif m == "Treasure1" and n == False:
                                continue
                elif path[i][j] == "Treasure1" and path[i][j-1] == "Empty":
                    if path[i][j-1] == "Empty" and t1 == 1:
                        action.append('right')
                        for [m,n] in initial_state:
                            if m == "Treasure1" and n == True:
                                action.append('grab')
                            elif m == "Treasure1" and n == False:
                                continue
                    elif path[i][j-1] == "Empty" and t1counter == 1:
                        action.append('right')
                        for [m,n] in initial_state:
                            if m == "Treasure1" and n == True:
                                action.append('grab')
                            elif m == "Treasure1" and n == False:
                                continue
                        t1counter += 1
                    elif path[i][j-1] == "Empty" and t1counter > 1:
                        action.append('right')
                        for [m,n] in initial_state:
                            if m == "Treasure1" and n == True:
                                continue
                            elif m == "Treasure1" and n == False:
                                continue
                
            j += 1
        i += 1
    action.append('escape')
    return action


def visited(child,initial_state,goal_state):
    checklist = ["Empty","Treasure0","Treasure1","Light"]
    result =  all(elem in child  for elem in checklist)
    visit = []
    count = 0
    t0 = child.count("Treasure0")
    t1 = child.count("Treasure1")
    l = child.count("Light")
    t0counter = 1
    t1counter = 1
    lightcounter = 1

    for a in child:
        if result == False:
            if a == "Treasure0":
                if t0 == 1:
                    for [m,n] in initial_state:
                        if a == m and a == "Treasure0":
                            if n == False:
                                visit.append([a,False])
                            elif n == True:
                                visit.append([a,False])
                else:
                    if t0counter == 1:
                        for [m,n] in initial_state:
                            if a == m and a == "Treasure0":
                                if n == False:
                                    visit.append([a,False])
                                elif n == True:
                                    visit.append([a,False])
                        t0counter += 1
                    elif t0counter > 1:
                        for [m,n] in initial_state:
                            if a == m and a == "Treasure0":
                                visit.append([a,False])
            elif a == "Treasure1":
                if t1 == 1:
                    for [m,n] in initial_state:
                        if a == m and a == "Treasure1":
                            if n == False:
                                visit.append([a,False])
                            elif n == True:
                                visit.append([a,False])
                else:
                    if t1counter == 1:
                        for [m,n] in initial_state:
                            if a == m and a == "Treasure1":
                                if n == False:
                                    visit.append([a,False])
                                elif n == True:
                                    visit.append([a,False])
                        t1counter += 1
                    elif t1counter > 1:
                        for [m,n] in initial_state:
                            if a == m and a == "Treasure1":
                                visit.append([a,False])
            elif a == "Light":
                if l == 1:
                    for [m,n] in initial_state:
                        if a == m and a == "Light":
                            if n == False:
                                visit.append([a,True])
                            elif n == True:
                                visit.append([a,True])
                else:
                    if lightcounter == 1:
                        for [m,n] in initial_state:
                            if a == m and a == "Light":
                                if n == False:
                                    visit.append([a,True])
                                elif n == True:
                                    visit.append([a,True])
                        lightcounter += 1
                    elif lightcounter > 1:
                        for [m,n] in initial_state:
                            if a == m and a == "Light":
                                visit.append([a,True])
        elif result == False and a == "Empty":
            for [m,n] in initial_state:
                if a == m and a == "Empty":
                    visit.append([a,False])
        elif result == True:
            if a == "Treasure0":
                if t0 == 1:
                    for [m,n] in initial_state:
                        if a == m and a == "Treasure0":
                            if n == False:
                                visit.append([a,False])
                            elif n == True:
                                visit.append([a,False])
                else:
                    if t0counter == 1:
                        for [m,n] in initial_state:
                            if a == m and a == "Treasure0":
                                if n == False:
                                    visit.append([a,False])
                                elif n == True:
                                    visit.append([a,False])
                        t0counter += 1
                    elif t0counter > 1:
                        for [m,n] in initial_state:
                            if a == m and a == "Treasure0":
                                visit.append([a,False])
            elif a == "Treasure1":
                if t1 == 1:
                    for [m,n] in initial_state:
                        if a == m and a == "Treasure1":
                            if n == False:
                                visit.append([a,False])
                            elif n == True:
                                visit.append([a,False])
                else:
                    if t1counter == 1:
                        for [m,n] in initial_state:
                            if a == m and a == "Treasure1":
                                if n == False:
                                    visit.append([a,False])
                                elif n == True:
                                    visit.append([a,False])
                        t1counter += 1
                    elif t1counter > 1:
                        for [m,n] in initial_state:
                            if a == m and a == "Treasure1":
                                visit.append([a,False])
            elif a == "Light":
                if l == 1:
                    for [m,n] in initial_state:
                        if a == m and a == "Light":
                            if n == False:
                                visit.append([a,True])
                            elif n == True:
                                visit.append([a,True])
                else:
                    if lightcounter == 1:
                        for [m,n] in initial_state:
                            if a == m and a == "Light":
                                if n == False:
                                    visit.append([a,True])
                                elif n == True:
                                    visit.append([a,True])
                        lightcounter += 1
                    elif lightcounter > 1:
                        for [m,n] in initial_state:
                            if a == m and a == "Light":
                                visit.append([a,True])
            elif a == "Empty":
                for [m,n] in initial_state:
                    if a == m and a == "Empty":
                        visit.append([a,True])
        count += 1
    return visit


def goal(visits, goal_state):
    [i for e in visits for i in goal_state if e in i]
    if sorted(visits) == sorted(goal_state):
        return True
    else:
        return False
    

initial_state = [["Empty",False],["Treasure0",False],["Treasure1",True],["Light",False]]
goal_state = [["Empty", True], ["Treasure0",False],["Treasure1",False],["Light",True]]

listofrooms = ['Empty','Treasure0','Treasure1','Light']

def bfs(initial_state, goal_state, state_space,listofrooms):
    frontier = []
    newfrontier = []
    explored = []
    newexplored = []
    found_goal = False
    escaped = False
    frontier.append([random.choice(listofrooms)])

    while not found_goal:
        children = expandAndReturnChildren(state_space, frontier[0])
        explored.append(frontier[0][-1])
        
        del frontier[0]
    
        for child in children:
        
            visits = visited(child,initial_state,goal_state)
            gs = goal(visits, goal_state)
            if gs == True:
                newfrontier.append([child[-1]])
                found_goal = True
                solution = child
            frontier.append(child)
        frontier = sortFrontier(frontier, state_space)

        print("Explored: ")
        print(explored)
        print("Frontier:")
        for f in frontier:
            print(f)
        print("Children: ")    
        print(children)
        print("")

    print("Solution ", solution)
    
    while not escaped:
        newchildren = newExpandAndReturnChildrend(state_space, newfrontier[0])
        newexplored.append(newfrontier[0][-1])
        del newfrontier[0]
                
        for newchild in newchildren:
            if not (newchild[-1] in newexplored) and not (newchild[-1] in [f[-1] for f in newfrontier]):
                if "Empty" in newchild:
                    escaped = True
                    newchild.pop(0)
                    route = newchild
                newfrontier.append(newchild)

        newfrontier = sortFrontier(newfrontier, state_space)
        print("Explored: ")
        print(newexplored)
        print("Frontier:")
        for f in newfrontier:
            print(f)
        print("Children: ")    
        print(newchildren)
        print("")
    print(route)
    
    path = [solution + route]
    a = pathAndAction(path,initial_state)
    return a

a = bfs(initial_state,goal_state,state_space,listofrooms)
print(a)

