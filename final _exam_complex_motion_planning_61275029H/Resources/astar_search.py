
def a_star_search( initial, successor_func, is_goal_func, heur_func, node_limit = 1000, depth_limit = None, ax = None ):
    queue = [ ( initial, heur_func(initial), 0, [initial] ) ]
    num_nodes = 1
    max_queue = 0
    sol = None
    visited = [ ]
    frames = []

    #print("Search started", queue)
    while( len( queue ) > 0 ):
        # queue = queue[0:-1]
        #print("Q", queue)
        if ( len(queue) > max_queue ):
              max_queue = len(queue)
        current, current_h, current_g, chist = queue.pop()
        visited.append( current )
        if ax is not None:
          #print('visited', visited )
          frame = drawEnvironment( ax, env, visited )
          frames.append( frame )

        #print('   ' * len(chist), current, '[', chist, ']' )
        #print("Num Nodes", numNodes)
        #print( len(chist), depthLimit, printState( current ) )
        if is_goal_func( current ):
            sol = chist
            break
        if ( depth_limit is None ) or ( len(chist) <= depth_limit ):
            # print("current state", current, current_h, current_g, chist )
            # print("queue", queue)
            children = successor_func( current )
            #print("children", children)
            for child in children:
                c, cost = child
                if c not in chist:
                    #print("Add child", printState(c))
                    h = heur_func( c )
                    g = current_g + cost
                    pos = 0
                    for i in range(len(queue)-1, -1, -1 ):
                      if ( queue[i][1] + queue[i][2] >= h + g ):
                        pos = i + 1
                        break
                    queue.insert(pos, (c, h, g, chist + [c] ))
                    num_nodes = num_nodes + 1
                    if ( num_nodes > node_limit ):
                        #print("search terminated with num_nodes", num_nodes )
                        return ( num_nodes, max_queue, None )
        # else:
        #   print("Depth cutoff", len(chist), ">", depth_limit )
    return ( num_nodes, max_queue, sol, frames )
