from extract_and_load import EL
import pytest

def test_hello_world() :
    EL.hello_world()


def test_transform_yyyymmdd_date():
    date = "2022/07/16"
    assert(EL.transform_date(date) == "20220716")