import re


class Parameter(object):
    def __init__(self, name: str, type_: str):
        p = re.compile(r"(?P<name>\w+\[?\]?)=?(?P<default>.+)?")
        m = p.match(name)
        # name attribute
        self.name = m.group('name')
        # type attribute
        self.type = type_.replace('const ', '')
        self.type = self.type.replace('&', '')
        # default attribute
        self.default = m.group('default')
        # is_enum attribute
        p = re.compile(r"\b[ENUM|enum]{1}[_A-Za-z]+")
        self.is_enum = bool(p.search(type_))
        # is_constant attribute
        p = re.compile(r"const\s")
        self.is_constant = bool(p.search(type_))
        # passed_by_reference attribute
        p = re.compile(r"[A-Za-z_]+\&")
        self.passed_by_reference = bool(p.search(type_))
        # is_array attribute
        p = re.compile(r"[A-Za-z_]+\[\]")
        self.is_array = bool(p.search(name))


    def __str__(self):
        parameter_str = ''
        if self.is_constant:
            parameter_str += 'const '
        parameter_str += self.type
        if self.passed_by_reference:
            parameter_str += '& '
        else:
            parameter_str += ' '
        parameter_str += self.name
        if self.default is not None:
            parameter_str += f"={self.default}"
        return parameter_str


    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

