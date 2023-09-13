# include libraries
import random
import matplotlib.pyplot as plt
from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter

def quicksort(a, p, r, parent=None):
    if p < r:
        q = partition(a, p, r)
        node = Node(f"{a[q]}", parent=parent)
        quicksort(a, p, q - 1, parent=node)
        quicksort(a, q + 1, r, parent=node)

def partition(a, p, r):
    x = a[r]
    i = p - 1

    for j in range(p, r):  # for j = p to r - 1:
        if a[j] <= x:
            i = i + 1
            # swap
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    # swap
    temp2 = a[i + 1]
    a[i + 1] = a[r]
    a[r] = temp2
    return i + 1

def rseq(num):
    return [random.randint(0, num) for _ in range(num)]

def main():
    # a. 10, 80, 3, 19, 14, 7, 5, 12
    a = [10, 80, 3, 19, 14, 7, 5, 12]
    print("Unsorted - GIVEN sequence:\n", a)
    root = Node(f"{a[-1]}")
    quicksort(a, 0, len(a) - 1, parent=root)
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")
    print("\nSorted - GIVEN sequence: \n", a)

    # b. Choose your sequence with 100 different (random) integer numbers
    b = rseq(100)
    print(
        "\nUnsorted - sequence with",
        len(b),
        "different (random) integer numbers: \n",
        b,
    )
    root = Node(f"{b[-1]}")
    quicksort(b, 0, len(b) - 1, parent=root)
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")
    print(
        "\nSorted - sequence with", len(b), "different (random) integer numbers: \n", b
    )

    # Plot the tree using Matplotlib
    plt.figure(figsize=(10, 10))
    ax = plt.subplot(1, 1, 1)
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-0.1, 1.1)

    # Use UniqueDotExporter to generate the Graphviz DOT file
    UniqueDotExporter(root, nodeattrfunc=lambda node: f'label="{node.name}"').to_dotfile('quicksort_tree.dot')

    # Read the DOT file and draw the tree using Matplotlib
    with open('quicksort_tree.dot') as f:
        dot_graph = f.read()
    ax = plt.subplot(1, 1, 1)
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_xlim(-1.1, 1.1)
    ax.set
    ax.show()