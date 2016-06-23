# -*- coding: utf-8 -*-
"""
**************
Tree
**************
Tree class for constructing a tree data structure based on NetworkX
OrderedDiGraph.

"""

#    Copyright (C) 2016 by
#    Youngsung Kim<grnydawn@gmail.com>
#    All rights reserved.

from networkx.classes.ordered import OrderedDiGraph

class Tree(OrderedDiGraph):
    """
    A class for graph-based tree data structure

    Examples
    --------


    """

    def __init__(self, rootnode=None, **kwargs):
        """Initialize a tree with optional root node 

        Parameters
        ----------
        rootnode : input a hashable object
            rootnode to be set as a root of this tree
            If rootnode is None, user should set this explicitely
            by using set_rootnode method.

        """
        self.rootnode = rootnode
        super(Tree, self).__init__(**kwargs)

    def set_rootnode(self, rootnode):
        """Set a rootnode

        rootnode is a direct or indirect predecessor node of all other nodes in this tree

        Parameters
        ----------
        rootnode : input a hashable object
            rootnode to be set as a root of this tree
        """
        self.rootnode = rootnode

    def add_childnode(self, parentnode, childnode):
        """Add a child node to a parent node

        Parameters
        ----------
        parentnode : input a hashable object
            parentnode is a predecessor of childnode in a tree.
        """
        self.add_edge(parentnode, childnode)

