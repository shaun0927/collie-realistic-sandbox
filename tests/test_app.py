import pytest

from app import normalize_timeout, path_url, route_operation_id


def test_normalize_timeout_positive():
    assert normalize_timeout("1.5") == 1.5


def test_normalize_timeout_rejects_zero():
    with pytest.raises(ValueError):
        normalize_timeout(0)


def test_path_url_includes_query():
    assert path_url("https://example.test/a?b=1") == "/a?b=1"


def test_operation_id_includes_method():
    assert route_operation_id("/items", "GET") == "get_items_6"
