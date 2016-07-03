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

MOD_TYPES = [ ast.Module, ast.Interactive, ast.Expression, ast.Suite ]

STMT_TYPES = [ ast.FunctionDef, ast.ClassDef, ast.Return, ast.Delete, ast.Assign, ast.AugAssign, \
    ast.Print, ast.For, ast.While, ast.If, ast.With, ast.Raise, ast.TryExcept, ast.TryFinally, \
    ast.Assert, ast.Import, ast.ImportFrom, ast.Exec, ast.Global, ast.Expr, ast.Pass, ast.Break, \
    ast.Continue ]

EXPR_TYPES = [ ast.BoolOp, ast.BinOp, ast.UnaryOp, ast.Lambda, ast.IfExp, ast.Dict, ast.Set, \
    ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp, ast.Yield, ast.Compare, ast.Call, \
    ast.Repr, ast.Num, ast.Str, ast.Attribute, ast.Subscript, ast.Name, ast.List, ast.Tuple ]

TITLE_SIZE = 24


import danata

def genlabel(node):
    lines = []

    lines.append(node.__class__.__name__)

    #if hasattr(node, 'value'):
    #    lines.append( str(node.value) )

    return '\n'.join(lines)

def add_nodes(tree, node, nodeinfo, edgeinfo):
    """ Populates network
    """
    def add_node(tree, node, pnode, attr, nodeinfo, edgeinfo):
        """ Helper function that recursively adds nodes.
        """

        if pnode is None or isinstance(node, ast.AST):
            if node not in nodeinfo:
                nodeinfo[node] = {}
            nodeinfo[node]['label'] = genlabel(node)
            if node.__class__ in MOD_TYPES:
                nodeinfo[node]['type'] = MOD_TYPES
            elif node.__class__ in STMT_TYPES:
                nodeinfo[node]['type'] = STMT_TYPES
            elif node.__class__ in EXPR_TYPES:
                nodeinfo[node]['type'] = EXPR_TYPES
            else:
                nodeinfo[node]['type'] = None

            if pnode is None:
                tree.set_rootnode(node)
            elif isinstance(node, ast.AST):
                if (pnode, node) not in edgeinfo:
                    edgeinfo[(pnode, node)] = {}
                edgeinfo[(pnode, node)]['label'] = attr
                tree.add_childnode(pnode, node)

        # Recursively descent the AST 
        if isinstance(node, ast.AST):
            for key, val in ast.iter_fields(node):
                if key in BLOCK_TYPES:
                    try:
                        for subnode in val:
                            add_node(tree, subnode, node, key, nodeinfo, edgeinfo)
                    except:
                        add_node(tree, val, node, key, nodeinfo, edgeinfo)
                elif key not in ['ctx']:
                    if isinstance(val, ast.AST):
                        add_node(tree, val, node, key, nodeinfo, edgeinfo)
                    else:
                        valstr = str(val)
                        if len(valstr)>20:
                            valstr = '%s...'%valstr[:20]
                        nodeinfo[node]['label'] += '\n%s = %s'%(key, valstr)

    # End of helper function

    add_node(tree, node, None, None, nodeinfo, edgeinfo)

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
                    tree = danata.DNTTree()
                    rootnode = ast.parse(fobj.read(), filename=fpath)

                    nodeinfo = {}
                    edgeinfo = {}

                    add_nodes(tree, rootnode, nodeinfo, edgeinfo)

                    node_labels = {node: nodeinfo[node]['label'] for node in tree.nodes()}
                    node_colors = []
                    for node in tree.nodes():
                        if nodeinfo[node]['type']==MOD_TYPES:
                            node_colors.append(1.0)
                        elif nodeinfo[node]['type']==STMT_TYPES:
                            node_colors.append(0.6)
                        elif nodeinfo[node]['type']==EXPR_TYPES:
                            node_colors.append(0.3)
                        else:
                            node_colors.append(0.0)
                    edge_labels = {edge: edgeinfo[edge]['label'] for edge in tree.edges()}

                    #import pdb; pdb.set_trace()
                    nx.draw_networkx(tree, tree_layout(tree), with_labels=True, \
                        labels=node_labels, node_color=node_colors)
                    nx.draw_networkx_edge_labels(tree, tree_layout(tree), edge_labels, label=None)
            except:
                raise

    plt.title('Abstract Syntax Tree Diagram for "%s"'%fpath, fontsize=TITLE_SIZE)
    plt.show()

if __name__ == '__main__':
    main()
