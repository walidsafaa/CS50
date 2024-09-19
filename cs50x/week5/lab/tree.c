#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node* left;
    struct node* right;
}
node;

int search(node* tree, int number);

int main (void)
{
    node* tree = NULL;

    node* n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }

    n->number = 2;
    n->right = NULL;
    n->left = NULL;
    tree = n;

    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }

    n->number = 1;
    n->right = NULL;
    n->left = NULL;
    tree->left = n;

    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }

    n->number = 3;
    n->right = NULL;
    n->left = NULL;
    tree->right = n;

    search(tree, 4);
}

int search(node* tree, int number)
{
    if (tree == NULL)
    {
        printf("Not Found\n");
        return 1;
    }
    else if (number < tree->number)
    {
        printf("go left\n");
        return search(tree->left, number);
    }
    else if (number > tree->number)
    {
        printf("go right\n");
        return search(tree->right, number);
    }
    else
    {
        printf("Found\n");
        return 0;
    }
}