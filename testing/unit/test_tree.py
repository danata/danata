"""Testing DNTTree and its derived classes"""
import danata

def test_is_tree_available():
    """Test if DNTTree is available"""
    tree = danata.DNTTree()

    assert isinstance(tree, danata.DNTTree)
