def getChildren(x):
    Children = []
    if x[0] < 3:
        Children.append(((3,x[1]),x))
    if x[1] < 4:
        Children.append(((x[0],4),x))
    if x[0] > 0:
        Children.append(((0,x[1]),x))
    if x[1] > 0:
        Children.append(((x[0],0),x))
    if x[0] > 0 and x[1] < 4 and x[0]+x[1] <= 4:
        Children.append(((0, x[0]+x[1]),x))
    if x[0] > 0 and x[1] < 4 and x[0]+x[1] > 4:
        Children.append(((x[0]+x[1]-4,4),x))
    if x[1] > 0 and x[0] < 3 and x[0]+x[1] <= 3:
        Children.append(((x[0]+x[1],0),x))
    if x[1] > 0 and x[0] < 3 and x[0]+x[1] > 3:
        Children.append(((3,x[0]+x[1]-3),x))
    return Children


InitialState = (0,0)
GoalState = (0,2)
GoalFound = False
OpenQueue = [(InitialState,(-1,-1))]
ClosedList = []
while OpenQueue:
    x = OpenQueue.pop(0)
    ClosedList.append(x)
    print('Examined:',x[0])
    if x[0]==GoalState:
        GoalFound = True
        break
    Children = getChildren(x[0])
    ChildrenNew = list(Children)
    for i in Children:
        if i[0] in [j[0] for j in OpenQueue] or i[0] in [k[0] for k in ClosedList]:
            ChildrenNew.remove(i)
    OpenQueue = OpenQueue + ChildrenNew
if GoalFound:
    print('Goal found')
    SolutionPath = [x[0]]
    while x[1] != (-1,-1):
        for i in ClosedList:
            if i[0]==x[1]:
                x = i
        SolutionPath += [x[0]]
    SolutionPath.reverse()
    print(SolutionPath)
else:
    print('Goal not found')
