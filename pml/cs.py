'''
Template module to define control systems.
'''


class ControlSystem(object):

    def __init__(self):
        raise NotImplementedError()

    def get(self, pv):
        raise NotImplementedError()

    def put(self, pv, value):
        raise NotImplementedError()
