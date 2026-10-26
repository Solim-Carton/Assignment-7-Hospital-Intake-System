class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None
 
    def _find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        return self._find(node.left, name) or self._find(node.right, name)
 
    def insert(self, parent_name, name, side):
        """Add `name` under `parent_name` on 'left' or 'right'. Returns True on success."""
        if side not in ("left", "right"):
            print(f"Invalid side: {side}")
            return False
        parent = self._find(self.root, parent_name)
        if parent is None:
            print(f"Parent not found: {parent_name}")
            return False
        if getattr(parent, side) is not None:
            print(f"{parent_name} already has a {side} report")
            return False
        setattr(parent, side, DoctorNode(name))
        return True
 
    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)
 
    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)
 
    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]
 
# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")
 
    assert tree.preorder(tree.root) == ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]
    assert tree.inorder(tree.root) == ["Dr. Morgan", "Dr. Phan", "Dr. Carson", "Dr. Croft", "Dr. Goldsmith"]
    assert tree.postorder(tree.root) == ["Dr. Morgan", "Dr. Carson", "Dr. Phan", "Dr. Goldsmith", "Dr. Croft"]
 
    # Edge cases
    assert tree.insert("Dr. Nobody", "Dr. X", "left") is False   # missing parent
    assert tree.insert("Dr. Croft", "Dr. X", "middle") is False  # invalid side
    assert tree.insert("Dr. Croft", "Dr. X", "left") is False    # side already taken
    assert tree.preorder(None) == []                              # empty tree
    print("All doctor_tree tests passed")
 





