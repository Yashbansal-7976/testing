def insert(root, key):
    if root is None:
        return Node(key)
    
    current = root
    while True:
        if key < current.val:
            if current.left is None:
                current.left = Node(key)
                break
            current = current.left
        else:
            if current.right is None:
                current.right = Node(key)
                break
            current = current.right
    return root   
