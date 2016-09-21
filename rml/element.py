''' Representation of an element
@param element_type: type of the element
@param length: length of the element
'''
from rml.exceptions import PvException
from rml.units import UcPoly


class Element(object):

    def __init__(self, elem_identity, physics, **kwargs):
        '''
        Possible arguments for kwargs:

        :str elem_identity: identifier used to match an element to a pv
        :set elem_family: a set used to store families
        :param cs: type of control system to be used
        '''
        self._identity = elem_identity
        self._physics = physics
        self.families = set()
        self._uc = dict()
        self._devices = dict()

    def get_length(self):
        return self._physics.length

    def add_device(self, field, device, uc):
        self._devices[field] = device
        self._uc[field] = uc

    def add_to_family(self, family):
        self.families.add(family)

    def get_pv_value(self, field, handle, unit='machine', sim=False):
        if not sim:
            if field in self._devices:
                value = self._devices[field].get_value(handle)
                if unit == 'physics':
                    value = self._uc[field].machine_to_physics(value)
                return value
            else:
                raise PvException("No device associated with field {0}")
        else:
            value = self._physics.get_value(field, handle, unit)
            if unit == 'machine':
                value = self._uc[field].machine_to_physics(value)
            return value

    def put_pv_value(self, field, value, unit='machine', sim=False):
        if not sim:
            if field in self._devices:
                if unit == 'physics':
                    value = self._uc[field].physics_to_machine(value)
                self._devices[field].put_value(value)
            else:
                raise PvException('''There is no device associated with
                                     field {0}'''.format(field))
        else:
            if unit == 'machine':
                value = self._uc[field].machine_to_physics(value)
            self._physics.put_value(field, value)

    def get_pv_name(self, field, handle='*', sim=False):
        if not sim:
            if field in self._devices:
                return self._devices[field].get_pv_name(handle)
        else:
            return self._physics.get_pv_name(field, handle)
        raise PvException("There is no device associated with field {0}"
                          .format(field))
