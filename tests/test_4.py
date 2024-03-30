import os
import shutil

import pytest
import test_import

from zad4 import decode_qr, encode_qr

content = "Hello World!"


@pytest.fixture
def set_up_dir():
    os.makedirs("test_dir", exist_ok=True)
    yield


def test_encode_into_qr(set_up_dir):
    encode_qr(content, "test_dir/test.png")
    assert os.path.exists("test_dir/test.png")


def test_decode_qr(set_up_dir):
    encode_qr(content, "test_dir/test.png")
    assert decode_qr("test_dir/test.png") == content


def test_clean_up():
    shutil.rmtree("test_dir")
    assert not os.path.exists("test_dir")
