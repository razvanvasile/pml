from pml.exceptions import PvException
import pml


class Device(object):
    ''' Template module that represents a device. '''
    # should be a length parameter here
    def __init__(self, cs, rb_pv=None, sp_pv=None):
        '''
        Create a device with a control system and readback/setpoint pvs.
        '''
        self.rb_pv = rb_pv
        self.sp_pv = sp_pv
        self._cs = cs
        assert not (rb_pv is None and sp_pv is None)
        if rb_pv is not None:
            self.name = rb_pv.split(':')[0]
        elif sp_pv is not None:
            self.name = sp_pv.split(':')[0]
        else:
            raise PvException("Readback or setpoint pvs need to be given")

    def put_value(self, value):
        '''
        Set the pv value on a setpoint pv. If the setpoint pv doesn't exist raise
        a PvException.
        '''
        # Not sure if this method will need a handle flag to set
        # an initial value for readback pvs. Suppose not:
        if self.sp_pv is not None:
            self._cs.put(self.sp_pv, value)
        else:
            raise PvException("""This device {0} has no setpoint pv."""
                              .format(self.name))

    def get_value(self, handle):
        '''
        Get either the setpoint or readback pv valuue off a device.
        '''
        if handle == pml.RB and self.rb_pv:
            return self._cs.get(self.rb_pv)
        elif handle == pml.SP and self.sp_pv:
            return self._cs.get(self.sp_pv)

        raise PvException("""This device {0} has no {1} pv."""
                          .format(self.name, handle))

    def get_pv_name(self, handle='*'):
        '''
        Get a pv name given a handle. If no handle is given return both pvs.
        '''
        if handle == '*':
            return [self.rb_pv, self.sp_pv]
        elif handle == pml.RB:
            return self.rb_pv
        elif handle == pml.SP:
            return self.sp_pv
