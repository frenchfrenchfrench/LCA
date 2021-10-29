#geeksforgeeks.com

class Node:
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
 

def findPath( root, path, k):
 
    # Baes Case
    if root is None:
        return None


    if root.key == path or root.key == k :
        return root

    if path == k:
        return path.key

    dag = []
    i = 0

    while(i < len(path.pred)):
        j = 0
        while(j < len(k.pred)):
            if(path.pred[i].key == k.pred[j].key):
                dag.append(path[i].key)
                j = j + 1
            else:
                j = j+1
        i = i + 1
    if(dag == []):
        if(path.key > k.key):
            dag.append(findPath(root, path.pred[0], k))
        else:
            dag.append(findPath(root, path, k.pred[0]))

    return max(dag)


root = Node(1)
r2 = Node(2)
r3 = Node(3)
r4 = Node(4)
r5 = Node(5)
r6 = Node(6)
root.succ = [r2, r3, r4, r5]
r2.succ = [r4]
r2.pred = [root]
r3.succ = [r4, r5]
r3.pred = [root]
r4.succ = [r5]
r4.pred = [r2, r3, root]
r5.pred = [r3, r4, root]
r6.pred = [r4]
