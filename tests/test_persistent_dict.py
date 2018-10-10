import pickle
import os

import pytest
from persistent_dict import PersistentDict


TEST_CASES = [
    {'a': 12},
    {'a': {'b': 'c'}},
    {'a': None, True: False},
    {},
    {'d': {'e': {'e': {'p': 'nested'}}}}
]


@pytest.fixture
def tmpfile(tmpdir):
    return tmpdir.join('test.tmp')


@pytest.fixture
def tmpdict(tmpfile):
    class TmpPersistentDict(PersistentDict):
        _default_location = tmpfile
    return TmpPersistentDict


@pytest.mark.parametrize('test_data', TEST_CASES)
def test_creation_from_other_dict(tmpdict, test_data):
    """Check PersistentDict creation from other dict"""
    new_dict = tmpdict(test_data)
    assert new_dict.data == test_data


def test_create_from_keys(tmpdict):
    """PersistentDict can be created fromkeys"""
    test_dict = tmpdict.fromkeys(['a', 'b', 'c'], 'value')
    assert test_dict == {'a': 'value', 'b': 'value', 'c': 'value'}


@pytest.mark.parametrize('test_data', TEST_CASES)
def test_create_from_assignment(tmpdict, test_data):
    """Assignments should work as expected"""
    test_dict = tmpdict()
    for k, v in test_data.items():
        test_dict[k] = v
    assert test_dict == test_data


def test_get(tmpdict):
    """`get()` should work as expected"""
    test_dict = tmpdict()
    test_dict['a'] = 'test'
    assert test_dict.get('a') == 'test'
    assert test_dict.get('non-exist', False) is False


def test_clear(tmpfile):
    """Clear must also clear storage file"""
    test_dict = PersistentDict({'a': 42, 'b': 1464}, location=tmpfile)
    test_dict.clear()
    assert test_dict == {}
    assert not os.path.exists(tmpfile)


@pytest.mark.parametrize('test_data', TEST_CASES)
def test_read_from_file(tmpfile, test_data):
    """Should properly read from existing file"""
    with open(tmpfile, 'wb') as fh:
        fh.write(pickle.dumps(test_data))
    test_dict = PersistentDict(location=tmpfile)
    assert test_dict == test_data
