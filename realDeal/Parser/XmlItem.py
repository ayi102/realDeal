class XmlItem():

    def __init__(self, name: str, type: str, value : float):
        self._name        = name
        self._type        = type
        self._value       = value
        self._percent     = 100.00
        self._typePercent = 100.00

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def value(self):
        return self._value

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, val: float):
        self._percent = val

    @property
    def typePercent(self):
        return self._typePercent

    @typePercent.setter
    def typePercent(self, val: float):
        self._typePercent = val

    def __eq__(self, other):
        if other.name        == self.name    and \
           other.value       == self.value   and \
           other.type        == self.type    and \
           other.percent     == self.percent and \
           other.typePercent == self.typePercent:
            return True
        else:
            return False
