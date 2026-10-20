class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        node = TreeNode(key, val)
        if not self.root:
            self.root = node
            return
        
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = node
                    return
                curr = curr.left

            elif key > curr.key:
                if not curr.right:
                    curr.right = node
                    return
                curr = curr.right

            else:
                curr.val = val
                return


    def get(self, key: int) -> int:
        if not self.root:
            return -1
        
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
            
        return -1


    def recurseMin(self, root: TreeNode) -> TreeNode | None:
        if not self.root:
            return

        if root.left:
            return self.recurseMin(root.left)

        return root

    def getMin(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.left:
            curr = curr.left
        
        return curr.val


    def getMax(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.right:
            curr = curr.right
        
        return curr.val

    def recurseRemove(self, root: TreeNode, key: int):
        if not root:
            return
        
        if key < root.key:
            root.left = self.recurseRemove(root.left, key)
        elif key > root.key:
            root.right = self.recurseRemove(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_ = self.recurseMin(root.right)
                root.key = min_.key
                root.val = min_.val
                root.right = self.recurseRemove(root.right, min_.key)

        return root


    def remove(self, key: int) -> None:
        self.root = self.recurseRemove(self.root, key)


    def inorder(self, root: TreeNode, result: List[int]) -> None:
        if not root:
            return

        self.inorder(root.left, result)
        result.append(root.key)
        self.inorder(root.right, result)


    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorder(self.root, result)
        return result

