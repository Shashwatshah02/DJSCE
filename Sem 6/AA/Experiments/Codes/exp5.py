# Define the Node class to represent nodes in the KD tree
class Node:
    def __init__(self, nums):
        self.nums = nums  # Store the list of numbers representing a point in k-dimensional space
        self.level = 0  # Initialize the level or depth of the node
        self.left = None  # Initialize the left child pointer
        self.right = None  # Initialize the right child pointer

# Helper function to create a new node with the given list of numbers
def create_node(nums):
    return Node(nums)

# Function to perform an in-order traversal of the KD tree and print the points
def traverse_in_order(curr):
    if curr is None:
        return
    traverse_in_order(curr.left)  # Recursively traverse the left subtree
    print(f"({', '.join(map(str, curr.nums))}) ", end="")  # Print the point stored in the current node
    traverse_in_order(curr.right)  # Recursively traverse the right subtree

# Function to construct the KD tree from a sequence of points (seq) and a depth parameter
def make_kd_tree(seq, depth=0):
    if len(seq) == 0:
        return None  # Base case: If the sequence is empty, return None

    k = len(seq[0])  # Determine the number of dimensions (k) from the first point in the sequence
    dim = depth % k  # Calculate the dimension to split the points based on the current depth

    seq.sort(key=lambda x: x[dim])  # Sort the sequence based on the chosen dimension

    mid = len(seq) // 2  # Calculate the index of the median element
    mid_elem = seq[mid]  # Select the median element as the element to be stored in the current node

    root = create_node(mid_elem)  # Create a new node with the median element as the point

    left_sub_arr = seq[:mid]  # Split the sequence into left and right subarrays
    right_sub_arr = seq[mid+1:]

    root.level = depth  # Set the level of the current node to the current depth
    root.left = make_kd_tree(left_sub_arr, depth+1)  # Recursively construct the left subtree
    root.right = make_kd_tree(right_sub_arr, depth+1)  # Recursively construct the right subtree

    return root  # Return the constructed root node of the KD tree

# Main block
if __name__ == "__main__":
    # Sample sequence of points in 2-dimensional space
    seq = [[6,2], [7,1], [2,9], [3,6], [4,8], [8,4], [5,3], [1,5], [9,5]]

    # Create the KD tree using the make_kd_tree function and store the root node in root
    root = make_kd_tree(seq)

    # Perform an in-order traversal of the KD tree and print the points in sorted order
    print("Inorder Traversal: ", end='')
    traverse_in_order(root)
