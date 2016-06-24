"""Draw ASTs"""

import os
import sys
import ast
import types
import matplotlib.pyplot as plt
import networkx as nx

DANATA_HOME = '%s/../..'%os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, DANATA_HOME)
BLOCK_TYPES = ['body', 'orelse', 'handlers', 'decorator_list', 'bases', 'targets', 'values', \
    'finalbody', 'names', 'elts', 'generators', 'ops', 'comparators', 'args', 'keywords', \
    'dims', 'ifs', 'defaults']
TITLE_SIZE = 24

import danata

def genlabel(node):
    lines = []

    lines.append(node.__class__.__name__)

    #if hasattr(node, 'value'):
    #    lines.append( str(node.value) )

    return '\n'.join(lines)

def add_nodes(tree, node, node_labels, edge_labels):
    """ Populates network
    """
    def add_node(tree, node, pnode, attr, node_labels, edge_labels):
        """ Helper function that recursively adds nodes.
        """

        if pnode is None:
            node_labels[node] = genlabel(node)
            tree.set_rootnode(node)
        elif isinstance(node, ast.AST):
            node_labels[node] = genlabel(node)
            edge_labels[(pnode, node)] = attr
            tree.add_childnode(pnode, node)

        # Recursively descent the AST 
        if isinstance(node, ast.AST):
            for key, val in ast.iter_fields(node):
                if key in BLOCK_TYPES:
                    try:
                        for subnode in val:
                            add_node(tree, subnode, node, key, node_labels, edge_labels)
                    except:
                        add_node(tree, val, node, key, node_labels, edge_labels)
                        pass
                elif key not in ['ctx']:
                    if isinstance(val, ast.AST):
                        add_node(tree, val, node, key, node_labels, edge_labels)
                    else:
                        valstr = str(val)
                        if len(valstr)>20:
                            valstr = '%s...'%valstr[:20]
                        node_labels[node] += '\n%s = %s'%(key, valstr)

    # End of helper function

    add_node(tree, node, None, None, node_labels, edge_labels)

## BFS
#def tree_layout(tree):
#    pos = {}
#    pos[tree.rootnode] = (0, 0)
#
#    queue = [(tree.rootnode, 0, 0)]
#    while queue:
#        vertex, px, py = queue.pop(0)
#        for i, subnode in enumerate(tree.successors(vertex)):
#            pos[subnode] = (px+i, py-1)
#            queue.append((subnode, px+i, py-1))
#
#    return pos

# DFS
#def tree_layout(tree):
#
#    def pos_node(node, px, py, pos):
#        i = 0
#        j = 0
#        for i, subnode in enumerate(tree.successors(node)):
#            pos_x = px + i + j
#            pos_y = py - 1
#            pos[subnode] = (pos_x, pos_y)
#            j += pos_node(subnode, pos_x, pos_y, pos)
#        return i+j
#
#    pos = {}
#    pos[tree.rootnode] = (0, 0)
#    pos_node(tree.rootnode, 0, 0, pos)
#
#    return pos
def tree_layout(tree):
    LINE_SPACE = 2
    def pos_node(node, px, py, pos):
        i = 0
        j = 0
        for i, subnode in enumerate(tree.successors(node)):
            pos_x = px + 1
            pos_y = py - i*LINE_SPACE - j
            pos[subnode] = (pos_x, pos_y)
            j += pos_node(subnode, pos_x, pos_y, pos)
        return i*LINE_SPACE + j

    pos = {}
    pos[tree.rootnode] = (0, 0)
    pos_node(tree.rootnode, 0, 0, pos)

    return pos


def main():
    """
    main function to drive overall execution


    processing steps
    ---------------

    1. AST generation of input Python source file
    2.
    """
    for fpath in sys.argv[1:]:
        if os.path.isfile(fpath):
            try:
                with open(fpath, 'r') as fobj:
                    tree = danata.Tree()
                    rootnode = ast.parse(fobj.read(), filename=fpath)

                    node_labels = {}
                    edge_labels = {}
                    add_nodes(tree, rootnode, node_labels, edge_labels)

                    nx.draw_networkx(tree, tree_layout(tree), with_labels=True, labels=node_labels, node_color='w')
                    nx.draw_networkx_edge_labels(tree, tree_layout(tree), edge_labels, label=None)
            except:
                raise

    plt.title('Abstract Syntax Tree Diagram for %s'%fpath, fontsize=TITLE_SIZE)
    plt.show()

if __name__ == '__main__':
    main()
