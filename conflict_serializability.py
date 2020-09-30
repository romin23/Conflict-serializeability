non_serial_operation = []
t1_list = []
t2_list = []
t3_list = []


while True:
    operations = input('Enter your Non Serial transactions one by one (ex : r1x): ').lower()
    if  operations == 'done' :
        print('Okay Completed')
        break
    non_serial_operation.append(operations)
# print(non_serial_operation)


for i in non_serial_operation:
    if i[1] == '1':
        t1_list.append(i)
    elif i[1] == '2':
        t2_list.append(i)
    elif i[1] == '3':
        t3_list.append(i)
# print(t1_list,t2_list, t3_list)


conflict_pair_list = []


for i in non_serial_operation:
    
    if i[0] == 'r':
        if i[1] == '1':
            for j in t2_list:
                pair_list = []
                pair_list.append(i)
                if j[0] == 'w' and j[-1] == i[-1]:
                    pair_list.append(j)
                    conflict_pair_list.append(pair_list)
                    
            for j in t3_list:
                pair_list = []
                pair_list.append(i)
                if j[0] == 'w' and j[-1] == i[-1]:
                    pair_list.append(j)
                    conflict_pair_list.append(pair_list)
                               
            
            t1_list.remove(i)
        elif i[1] == '2':
            for j in t1_list:
                pair_list = []
                pair_list.append(i)
                if j[0] == 'w' and j[-1] == i[-1]:
                    pair_list.append(j)
                    conflict_pair_list.append(pair_list)
                    
            for j in t3_list:
                pair_list = []
                pair_list.append(i)
                if j[0] == 'w' and j[-1] == i[-1]:
                    pair_list.append(j)
                    conflict_pair_list.append(pair_list)
                               
            
            t2_list.remove(i)
        elif i[1] == '3':
            for j in t2_list:
                pair_list = []
                pair_list.append(i)
                if j[0] == 'w' and j[-1] == i[-1]:
                    pair_list.append(j)
                    conflict_pair_list.append(pair_list)
                    
            for j in t1_list:
                pair_list = []
                pair_list.append(i)
                if j[0] == 'w' and j[-1] == i[-1]:
                    pair_list.append(j)
                    conflict_pair_list.append(pair_list)
                               
            
            t3_list.remove(i)
        
    elif i[0] == 'w':
        if i[1] == '1':
            for j in t2_list:
                pair_list = []
                pair_list.append(i)
                if j[-1] == i[-1]:
                    pair_list.append(j)
                    conflict_pair_list.append(pair_list)
                    
            for j in t3_list:
                pair_list = []
                pair_list.append(i)
                if j[-1] == i[-1]:
                    pair_list.append(j)
                    conflict_pair_list.append(pair_list)
                             
            
            t1_list.remove(i)
        elif i[1] == '2':
            for j in t1_list:
                pair_list = []
                pair_list.append(i)
                if j[-1] == i[-1]:
                    pair_list.append(j)
                    conflict_pair_list.append(pair_list)
                    
            for j in t3_list:
                pair_list = []
                pair_list.append(i)
                if j[-1] == i[-1]:
                    pair_list.append(j)
                    conflict_pair_list.append(pair_list)
                               
            
            t2_list.remove(i)
        elif i[1] == '3':
            for j in t2_list:
                pair_list = []
                pair_list.append(i)
                if j[-1] == i[-1]:
                    pair_list.append(j)
                    conflict_pair_list.append(pair_list)
                    
            for j in t1_list:
                pair_list = []
                pair_list.append(i)
                if j[-1] == i[-1]:
                    pair_list.append(j)
                    conflict_pair_list.append(pair_list)
                              
            
            t3_list.remove(i)

print('CONFLICTING PAIRS ARE: ')
for i  in conflict_pair_list:
    print(i)    



adj = {}


for i in conflict_pair_list:
    key = i[0][1]
    adj.setdefault(key,set())
    adj[key].add(i[1][1])


color = {}


for u in adj.keys():
    color[u] = 'W'
    

def dfs(u , color ):
    color[u] = "G"
    # print(u)
    for v in adj[u]:
        try: 
            if color[v] == 'W':
                dfs(v , color)
                if cycle_present == True:
                    return True
            elif color[v] == 'G':
                # print('CYCLE FOUND in GRAPH at NODE',u,',',v)
                return True
        except :
            return False
    color[u] = "B"
    return False


cycle_present = False


for u in adj.keys():
    if color[u] == "W":
        cycle_present =dfs(u, color)
        if cycle_present == True:
            print('As the graph is cyclic we can conclude that Schedule is NOT CONFLICT SERIALIZABLE')
            break
        elif  cycle_present == False:
            print('Graph is ACYCLIC Hence the Schedule is CONFLICT SERIALIZABLE')
