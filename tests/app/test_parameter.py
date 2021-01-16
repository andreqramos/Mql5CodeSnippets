import pytest
from src.app.parameter import Parameter


class TestParameterName(object):
    def test_parameter_name_equals_indicator_handle(self):
        parameter = Parameter('indicator_handle', 'int')
        assert parameter.name == 'indicator_handle'


    def test_parameter_name_equals_chart_id(self):
        parameter = Parameter('chart_id=0', 'long')
        assert parameter.name == 'chart_id'
    

    def test_parameter_name_equals_array(self):
        parameter = Parameter('array[]', 'const void&')
        assert parameter.name == 'array[]'


class TestParameterType(object):
    def test_parameter_type_equals_int(self):
        parameter = Parameter('indicator_handle', 'int')
        assert parameter.type == 'int'


    def test_parameter_type_equals_long(self):
        parameter = Parameter('chart_id=0', 'long')
        assert parameter.type == 'long'
    

    def test_parameter_type_equals_void(self):
        parameter = Parameter('array[]', 'const void&')
        assert parameter.type == 'void'


class TestParameterDefaultValue(object):
    def test_parameter_default_value_equals_none(self):
        parameter = Parameter('indicator_handle', 'int')
        assert parameter.default is None 


    def test_parameter_default_value_equals_0(self):
        parameter = Parameter('chart_id=0', 'long')
        assert parameter.default == '0'


class TestParameterIsEnum(object):
    def test_parameter_isenum_equals_false(self):
        parameter = Parameter('indicator_handle', 'int')
        assert not parameter.is_enum


    def test_parameter_isenum_equals_true(self):
        parameter = Parameter('property_id', 'ENUM_ACCOUNT_INFO_DOUBLE')
        assert parameter.is_enum


class TestParameterIsConstant(object):
    def test_parameter_isconstant_equals_false(self):
        parameter = Parameter('indicator_handle', 'int')
        assert not parameter.is_constant


    def test_parameter_isconstant_equals_true(self):
        parameter = Parameter('array[]', 'const void&')
        assert parameter.is_constant


class TestParameterPassedByReference(object):
    def test_parameter_passedbyreference_equals_false(self):
        parameter = Parameter('indicator_handle', 'int')
        assert not parameter.passed_by_reference


    def test_parameter_passedbyreference_equals_true(self):
        parameter = Parameter('array[]', 'const void&')
        assert parameter.passed_by_reference


class TestParameterIsArray(object):
    def test_parameter_isarray_equals_false(self):
        parameter = Parameter('indicator_handle', 'int')
        assert not parameter.is_array


    def test_parameter_isarray_equals_true(self):
        parameter = Parameter('array[]', 'const void&')
        assert parameter.is_array


class TestParameterToStr(object):
    def test_parameter_to_str_equals_int_indicator_handle(self):
        parameter = Parameter('indicator_handle', 'int')
        assert str(parameter) == 'int indicator_handle'
    

    def test_parameter_to_str_equals_const_void_array(self):
        parameter = Parameter('array[]', 'const void&')
        assert str(parameter) == 'const void& array[]'


    def test_parameter_to_str_equals_long_chart_id(self):
        parameter = Parameter('chart_id=0', 'long')
        assert str(parameter) == 'long chart_id=0'


class TestParametersEquals(object):
    def test_parameters_are_equals_case_1(self):
        parameter1 = Parameter('indicator_handle', 'int')
        parameter2 = Parameter('indicator_handle', 'int')
        assert parameter1 == parameter2


    def test_parameters_are_equals_case_2(self):
        parameter1 = Parameter('array[]', 'const void&')
        parameter2 = Parameter('array[]', 'const void&')
        assert parameter1 == parameter2


    def test_parameters_are_not_equals_case_1(self):
        parameter1 = Parameter('indicator_handle', 'int')
        parameter2 = Parameter('indicator_handle', 'any')
        assert parameter1 != parameter2


    def test_parameters_are_not_equals_case_2(self):
        parameter1 = Parameter('indicator_handle', 'int')
        parameter2 = Parameter('any', 'int')
        assert parameter1 != parameter2


    def test_parameters_are_not_equals_case_3(self):
        parameter1 = Parameter('indicator_handle', 'int')
        parameter2 = Parameter('any', 'any')
        assert parameter1 != parameter2


    def test_parameters_are_not_same_instances_1(self):
        parameter1 = Parameter('indicator_handle', 'int')
        parameter2 = ""
        assert parameter1 != parameter2


    def test_parameters_are_not_same_instances_2(self):
        parameter1 = Parameter('indicator_handle', 'int')
        parameter2 = []
        assert parameter1 != parameter2

