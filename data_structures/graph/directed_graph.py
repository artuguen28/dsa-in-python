from queue import Queue

def printBFS(graph: dict):

    if not graph:
        return
    
    visited = set()
    q = Queue()

    start_node = next(iter(graph))
    visited.add(start_node)
    q.put(start_node)

    while not q.empty():

        current = q.get()
        print(current, end=" ")

        for node in graph[current]:
            if node not in visited:
                visited.add(node)
                q.put(node)

    print()


    
    

if __name__ == "__main__":

    graph = {
        5:[2,8], 
        8:[1,3,4],
        2:[7], 
        4:[2,7,9], 
        3:[],
        1:[],
        7:[],
        9:[]
    }

    printBFD(graph)


