# -*- coding: utf-8 -*-
"""
IDE: Spyder (Python 3.8)
@author: Kevin Tudor
Course: Design and Analysis of Algorithms
Programming 2: BST
Due: April 24, 2023 (Monday), 11:59PM
"""

# include libraries
import matplotlib.pyplot as plt

class Node:
    #Node constructor
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    #initialize root by (First In)
    if root is None:
        print("Insert: ", key)
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def delete(root, key):
    if root is None:
        return root
    if root.key == key:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            pred = pre(root.left)
            root.key = pred.key
            root.left = delete(root.left, pred.key)
            print("Delete: ", key)
    #left children
    elif key < root.key:
        root.left = delete(root.left, key)
    #right children
    else:
        root.right = delete(root.right, key)
    return root

# Predeseccor: maximum value of left child (called by the left child of target)
def pre(root):
    if not root.right:
        return root
    return pre(root.right)

#search helper function
def search(root, key):
    path = []
    print("Searching tree for:", key)
    fig, (ax, ax2)= plt.subplots(2, figsize=(12, 12))
    ax.set_title(f"BST (a): Search PATH Key {key}")
    ax.set_axis_off()
    ax2.set_title(f"BST (a): Search TREE Key {key}")
    ax2.set_axis_off()
    search_plot(root, key, ax, path)
    search_tree(root, key, ax2, path)
    plt.show()

#plot search path recursive
def search_plot(root, key, ax, path, x=0, y=0, dx=1, dy=1):
    a, b = 0.1, 0.2
    if root is None: 
        print("Key not in BST")
        return
    # Path node
    path.append(root.key)
    ax.text(x, y, str(root.key), fontsize=20, ha='center', va='center',
                bbox=dict(facecolor='y', edgecolor='black', boxstyle='circle'))
    if root.key == key:
        print("Path: ", path)
        print("Found key:", key)
        return
    #left children
    if key < root.key:
        ax.arrow(x, y, -dx + a, -dy + b, head_width=a, head_length=a, fc='b', ec='k')
        search_plot(root.left, key, ax, path, x - dx, y - dy, dx , dy)
    #right children
    else:
        ax.arrow(x, y, dx - a, -dy + b, head_width=a, head_length=a, fc='b', ec='k')
        search_plot(root.right, key, ax, path, x + dx, y - dy, dx, dy)
    
        
#plot search on tree recursive
def search_tree(root, key, ax2, path, x=0, y=0, dx=1, dy=1, p = 0):
    a, b, c, d, e = 0.1, 0.3, 0.12, 0.1, 1.5
    if root:
        if root.key == path[p]: 
            # Plot yellow PATH node
            ax2.text(x, y, str(root.key), fontsize=20, ha='center', va='center',
                bbox=dict(facecolor='y', edgecolor='black', boxstyle='circle'))
            if p < len(path)-1:
                p += 1
        # Plot green node
        else:
            ax2.text(x, y, str(root.key), fontsize=20, ha='center', va='center',
                bbox=dict(facecolor='green', edgecolor='black', boxstyle='circle'))
        # left children
        if root.left:
            if root.left.key == path[p]:
                ax2.arrow(x, y, -dx + a, -dy + b, head_width=c, head_length=d, fc='b', ec='k')
                search_tree(root.left, key, ax2, path, x - dx, y - dy, dx / e, dy, p)
            else:
                ax2.arrow(x, y, -dx + a, -dy + b, head_width=c, head_length=d, fc='k', ec='k')
                search_tree(root.left, key, ax2, path, x - dx, y - dy, dx / e, dy, p)
        # right children
        if root.right:
            if root.right.key == path[p]:
                ax2.arrow(x, y, dx - a, -dy + b, head_width=c, head_length=d, fc='b', ec='k')
                search_tree(root.right, key, ax2, path, x + dx, y - dy, dx / e, dy, p)
            else:
                ax2.arrow(x, y, dx - a, -dy + b, head_width=c, head_length=d, fc='k', ec='k')
                search_tree(root.right, key, ax2, path, x + dx, y - dy, dx / e, dy, p)
   
#plot helper         
def plot(root, title):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_title(title)
    ax.set_axis_off()
    plot_tree(root, ax)
    plt.show()

#plot entire tree
def plot_tree(root, ax, x=0, y=0, dx=1, dy=1):
    a, b, c, d = 0.1, 0.3, 0.12, 1.5
    if root:
        # Plot node
        ax.text(x, y, str(root.key), fontsize=20, ha='center', va='center',
                bbox=dict(facecolor='green', edgecolor='black', boxstyle='circle'))
        # left children
        if root.left:
            ax.arrow(x, y, -dx + a, -dy + b, head_width=c, head_length=a, fc='k', ec='k')
            plot_tree(root.left, ax, x - dx, y - dy, dx / d, dy)
        # right children
        if root.right:
            ax.arrow(x, y, dx - a, -dy + b, head_width=c, head_length=a, fc='k', ec='k')
            plot_tree(root.right, ax, x + dx, y - dy, dx / d, dy)

def main():
    #Create tree
    print("--Generating tree--\n")
    nodes = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    BST = Node(nodes[0])
    print("Root insert: ", nodes[0])
    for val in nodes:
        if val != nodes[0]:
            BST = insert(BST, val)
    plot(BST, "Original BST")
    print("\n--Original tree generated--\n")
    
    #(a) Search key of node 6
    print("--(a) Search key of node 6--\n")
    search(BST, 6)
    
    #(b) Insert 5 into BST
    print("\n--(b) Insert 5 into BST--\n")
    BST = insert(BST, 5)
    plot(BST, "BST (b): Insert 5")
    
    #(c) Delete 6 from BST
    print("\n--(c) Delete 6 from BST--\n")
    BST = delete(BST, 6)
    plot(BST, "BST (c): Delete 6")
    
if __name__ == "__main__":
    main()