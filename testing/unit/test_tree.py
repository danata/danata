"""Testing Tree and its derived classes"""
import danata

def test_is_tree_available():
    """Test if Tree is available"""
    tree = danata.Tree()

    assert isinstance(tree, danata.Tree)
