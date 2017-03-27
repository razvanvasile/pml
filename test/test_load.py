import os
import pytest
from pml import load_csv


CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture
def lattice():
    lat = load_csv.load(os.path.join(CURRENT_DIR, 'data/dummy'))
    return lat


def test_elements_loaded(lattice):
    assert len(lattice) == 4
    assert lattice.get_all_families() == set(['drift', 'sext', 'quad'])
    assert len(lattice.get_elements('drift')) == 2
    assert len(lattice.get_elements('no_family')) == 0
    assert lattice.get_length() == 2.6


def test_devices_loaded(lattice):
    quads = lattice.get_elements('quad')
    assert len(quads) == 1
    assert quads[0].get_pv_name(field='b1', handle='readback') == 'Q1:RB'
    assert quads[0].get_pv_name(field='b1', handle='setpoint') == 'Q1:RB'
