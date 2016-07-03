# -*- coding: utf-8 -*-
"""
**************
DNTTree
**************
DNTTree class for constructing a tree data structure based on NetworkX
OrderedDiGraph.

"""

#    Copyright (C) 2016 by
#    Youngsung Kim<grnydawn@gmail.com>
#    All rights reserved.

from networkx.classes.ordered import OrderedDiGraph

class DNTTree(OrderedDiGraph):
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
        super(DNTTree, self).__init__(**kwargs)

    def set_rootnode(self, rootnode):
        """Set a rootnode

        rootnode is a direct or indirect predecessor node of all other nodes in this tree

        Parameters
        ----------
        rootnode : input a hashable object
            rootnode to be set as a root of this tree
        """
        self.rootnode = rootnode

    def add_childnode(self, parentnode, childnode, **kwargs):
        """Add a child node to a parent node

        Parameters
        ----------
        parentnode : input a hashable object
            parentnode is a predecessor of childnode in a tree.
        """
        self.add_edge(parentnode, childnode, **kwargs)

