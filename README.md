# Prüfer

A simple tool to convert Prüfer sequneces to trees.

Prüfer sequences are space-efficient representations of trees using a unique sequence. The sequence for a tree with *n* vertices has length *n - 2*. One can generate a labeled tree's Prüfer sequence by iteratively removing vertices from the tree until only two vertices remain.

## Installation

```
pip install prufer
```

## Usage

```
>>> import prufer
>>> prufer.build_tree([3, 3, 3, 4])
[(3, 0), (3, 1), (3, 2), (4, 3), (5, 4)]  # list of edges 
```

This corresponds to this tree (subtract all node labels by one):

![A sample prufer tree](img/tree-example.png)
