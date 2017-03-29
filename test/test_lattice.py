import pytest
import pml.lattice
import pml.element
import pml.device
import cs_dummy
import mock
from pml.units import UcPoly

DUMMY_NAME = 'dummy'


@pytest.fixture
def simple_element(identity=1):
    cs = cs_dummy.CsDummy()
    uc = UcPoly([0, 1])

    # Create devices and attach them to the element
    element = pml.element.Element(identity, 'element', mock.MagicMock())
    rb_pv = 'readback_pv'
    sp_pv = 'setpoint_pv'
    device1 = pml.device.Device(cs, sp_pv, rb_pv)
    device2 = pml.device.Device(cs, sp_pv, rb_pv)
    element.add_to_family('family')

    element.add_device('x', device1, uc)
    element.add_device('y', device2, uc)

    return element


@pytest.fixture
def simple_element_and_lattice(simple_element):
    l = pml.lattice.Lattice(DUMMY_NAME, mock.MagicMock())
    l.add_element(simple_element)
    return simple_element, l


def test_create_lattice():
    l = pml.lattice.Lattice(DUMMY_NAME, mock.MagicMock())
    assert(len(l)) == 0
    assert l.name == DUMMY_NAME


def test_non_negative_lattice():
    l = pml.lattice.Lattice(DUMMY_NAME, mock.MagicMock())
    assert(len(l)) >= 0


def test_lattice_with_n_elements(simple_element_and_lattice):
    elem, lattice = simple_element_and_lattice

    # Getting elements
    lattice.add_element(elem)
    assert lattice[0] == elem
    assert lattice.get_elements() == [elem, elem]


def test_lattice_get_element_with_family(simple_element_and_lattice):
    element, lattice = simple_element_and_lattice
    element.add_to_family('fam')
    assert lattice.get_elements('fam') == [element]
    assert lattice.get_elements('nofam') == []


def test_get_all_families(simple_element_and_lattice):
    element, lattice = simple_element_and_lattice
    families = lattice.get_all_families()
    assert len(families) > 0


def test_get_family_value(simple_element_and_lattice):
    element, lattice = simple_element_and_lattice
    lattice.get_family_value('family', 'x')
    lattice._cs.get.assert_called_with(['readback_pv'])
