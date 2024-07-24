# Initialize an empty output list
# Initialize an list of nodes to visit and add the root node to it
# While there are nodes in the nodes to visit list
#   Remove the first node from the nodes to visit list
#   Add its value to the output list
#   Add its children (if any) to the end of the nodes to visit list
# Return the output list

class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        return self._depth_first_search(self.root, id)

    def _depth_first_search(self, node, id):
        if node['id'] == id:
            return node
        for child in node['children']:
            result = self._depth_first_search(child, id)
            if result:
                return result
        return None
