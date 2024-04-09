#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;			//node will store some data
    struct node *right_child;	// right child
    struct node *left_child;	// left child
};

//function to create a node
struct node * new_node (int x)
{
    struct node *temp;
    temp = malloc (sizeof (struct node));
    temp->data = x;
    temp->left_child = NULL;
    temp->right_child = NULL;

    return temp;
}

// insertion
struct node * insert (struct node *root, int x)
{
  //searching for the place to insert
    if (root == NULL)
        return new_node (x);
    else if (x > root->data)	// x is greater. Should be inserted to the right
        root->right_child = insert (root->right_child, x);
    else				// x is smaller and should be inserted to left
        root->left_child = insert (root->left_child, x);
    return root;
}

// Inorder Traversal
void inorder(struct node *root) {
    if (root != NULL) // checking if the root is not null
    {
        inorder(root -> left_child); // traversing left child
        printf(" %d ", root -> data); // printing data at root
        inorder(root -> right_child); // traversing right child
    }
}

void preorder(struct node *root) {
    if (root != NULL) // checking if the root is not null
    {
        printf(" %d ", root -> data); // printing data at root
        preorder(root -> left_child); // traversing left child
        preorder(root -> right_child); // traversing right child
    }
}

void postorder(struct node *root) {
    if (root != NULL) // checking if the root is not null
    { 
        postorder(root -> left_child); // traversing left child
        postorder(root -> right_child); // traversing right child
        printf(" %d ", root -> data); // printing data at root
    }
}

int main() {
    struct node *root;
    root = new_node(20);
    insert(root, 5);
    insert(root, 1);
    insert(root, 15);
    insert(root, 9);
    insert(root, 7);
    insert(root, 12);
    insert(root, 30);
    insert(root, 25);
    insert(root, 40);
    insert(root, 45);
    insert(root, 42);

    inorder(root);
    printf("\n");
    preorder(root);
    printf("\n");
    postorder(root);
    printf("\n");
    return 0;
}
