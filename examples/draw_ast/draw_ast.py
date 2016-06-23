"""Draw ASTsn"""

import os
import sys
import ast
import matplotlib.pyplot as plt
import networkx as nx

DANATA_HOME = '%s/../..'%os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, DANATA_HOME)

import danata

#class Visitor(ast.NodeVisitor):
#    def generic_visit(self, node):
#        print 'Found a node class "%s"' % node.__class__
#
#        print 'dir(node) = %s' % [attr for attr in dir(node) if not attr.startswith('__')]
#        print 'node._attributes = %s' % str(node._attributes)
#        print 'node._fields = %s' % str(node._fields)
#        print 'node.body = %s' % str(node.body)
#        print 'node.body[0] = %s' % str(node.body[0])
#
#        print 'dir(node.body[0]) = %s' % [attr for attr in dir(node.body[0]) \
#           if not attr.startswith('__')]
#        print 'node.body[0]._attributes = %s' % str(node.body[0]._attributes)
#        print 'node.body[0]._fields = %s' % str(node.body[0]._fields)
#        print 'node.body[0].value = %s' % str(node.body[0].value)
#
#        print 'dir(node.body[0].value) = %s' % [attr for attr in dir(node.body[0].value) \
#           if not attr.startswith('__')]

def add_child_nodes(tree, parentnode, labels):
    """Add child nodes recursively"""
    for child_node in ast.iter_child_nodes(parentnode):
        tree.add_childnode(parentnode, child_node)
        labels[child_node] = str(child_node._attributes)
        add_child_nodes(tree, child_node, labels)

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
                tree = danata.Tree()
                rootnode = ast.parse(fpath)
                #Visitor().visit(topnode)

                tree.set_rootnode(rootnode)

                labels = {}
                labels[rootnode] = str(rootnode._attributes)

                add_child_nodes(tree, tree.rootnode, labels)

                nx.draw_networkx(tree, with_labels=True, labels=labels)
            except:
                raise

    plt.show()

if __name__ == '__main__':
    main()
