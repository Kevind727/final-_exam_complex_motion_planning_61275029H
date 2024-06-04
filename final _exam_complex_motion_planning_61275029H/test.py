map_points = [[20,30],[80,10],[50,50],[40,20],[50,50],[20,60],[20,50],[60,70],[80,20],[10,70],[80,40]]
map_roads = [[5,9],[3,6],[1,6],[1,3],[6,7],[5,7],[1,2],[7,8],[3,4],[3,9],[3,5],[3,8],[1,4],[5,8],[3,7],[6,8],[1,9],[1,5],[0,2],[0,6],[4,7],[8,9]]

def generate_neighborn(table,table_title,item):
    index=table_title.index(item)
    neighbor=[]
    for lotus in table[index]:
        if(lotus!=[]):
            neighbor+=[lotus]
                
    return  neighbor

table=[]

for x in range(0,len(map_points)):
    stap=[]
    for _ in range(0,len(map_points)):
        stap+=[[]]
    for y in range(0,len(map_roads)):
        if map_roads[y][0]==x :
            index=map_roads[y][1]
            stap[index]=map_points[index]
        
        if map_roads[y][1]==x :
            index=map_roads[y][0]
            stap[index]=map_points[index]
    table+=[stap]

print("%-10s"%" ",end="")

for x in map_points:
    print("%-10s"%str(x),end="")
print()
for y in range(0,len(table)):
    print("%-10s"%str(map_points[y]),end="")
    for x in range(0,len(table)):
        print("%-10s"%str(table[y][x]),end="")
    print()

lock_list=[]
from_list=[]
distance_list=[]

for lt in map_points:
    if(lt==[20,30]):
        lock_list+=[False]
        from_list+=[[-1,-1]]
        distance_list+=[0]
    else:
        lock_list+=[False]
        from_list+=[[]]
        distance_list+=[-1]


for _ in range(0,10):
    index=0
    min=max(distance_list)

    end=True
    for seq in range(0,len(distance_list)):
        if distance_list[seq]<=min and not(lock_list[seq]) and distance_list[seq]!=-1:
            index=seq
            min=distance_list[seq]
            end=False

            
    if(end):
        break

    now = map_points[index]
    lock_list[index] = True
    neighborn=generate_neighborn(table,map_points,now)
        
    for member in neighborn:
                
        now_id=map_points.index(now)
        member_id=map_points.index(member)
        if not(lock_list[member_id]):
            od=distance_list[now_id]
            dis=((member[0]-now[0])**2+(member[1]-now[1])**2)**0.5         
            distance_list[member_id]=od+dis
            from_list[member_id]=now

goal=[80,20]
path=[]

while goal!=[-1,-1]:
    path+=[goal]
    index=map_points.index(goal)
    goal=from_list[index]

path=list(reversed(path))
print(path)