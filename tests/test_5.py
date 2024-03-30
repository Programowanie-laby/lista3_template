import test_import

from zad5 import is_balanced


def test_if_true_is_balanced():
    assert is_balanced("()")
    assert is_balanced("{}")
    assert is_balanced("([][][])")
    assert is_balanced("([223+123]{90-0aa9})")
    assert is_balanced(" ")


def test_if_false_is_balanced():
    assert not is_balanced("(") 
    assert not is_balanced(")") 
    assert not is_balanced("]") 
    assert not is_balanced("}") 
    assert not is_balanced("([)]")
    assert not is_balanced("([]") 
