import pytest
from src.app.function import Function
from src.app.parameter import Parameter


barscalculated_cell = """
<td style="vertical-align:top; padding:3px; border:none">
    <p class="p_CodeExample" style="page-break-inside: avoid;">
        <span class="f_Keywords">int&nbsp;&nbsp; </span>
        <span class="f_Functions">BarsCalculated</span>
        <span class="f_CodeExample">(</span>
        <br>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Keywords">int</span>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Param">indicator_handle</span>
        <span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Comments">//&nbsp;indicator&nbsp;handle</span>
        <br>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;);</span>
    </p>
</td>"""
chartsymbol_cell = """
<td style="vertical-align:top; padding:3px; border:none">
    <p class="p_CodeExample" style="page-break-inside: avoid;">
        <span class="f_Keywords">string&nbsp;&nbsp;</span>
        <span class="f_Functions">ChartSymbol</span>
        <span class="f_CodeExample">(</span>
        <br>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Keywords">long</span>
        <span class="f_CodeExample">&nbsp;&nbsp;</span>
        <span class="f_Param">chart_id=0</span>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Comments">//&nbsp;Chart&nbsp;ID</span>
        <br>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;);</span>
    </p>
</td>"""
objectname_cell = """
<td style="vertical-align:top; padding:3px; border:none">
    <p class="p_CodeExample" style="page-break-inside: avoid;">
        <span class="f_Keywords">string&nbsp;&nbsp;</span>
        <span class="f_Functions">ObjectName</span>
        <span class="f_CodeExample">(</span>
        <br>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Keywords">long</span>
        <span class="f_CodeExample">&nbsp;&nbsp;</span>
        <span class="f_Param">chart_id</span>
        <span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Comments">//&nbsp;chart&nbsp;identifier</span>
        <br>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Keywords">int</span>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Param">pos</span>
        <span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Comments">//&nbsp;number&nbsp;in&nbsp;the&nbsp;list&nbsp;of&nbsp;objects</span>
        <br>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Keywords">int</span>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Param">sub_window=-1</span>
        <span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Comments">//&nbsp;window&nbsp;index</span>
        <br>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Keywords">int</span>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Param">type=-1</span>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        <span class="f_Comments">//&nbsp;object&nbsp;type</span>
        <br>
        <span class="f_CodeExample">&nbsp;&nbsp;&nbsp;);</span>
    </p>
</td>"""


class TestFunctionName(object):
    def test_function_name_equals_barscalculated(self):
        function = Function(barscalculated_cell)
        assert function.name == 'BarsCalculated'


    def test_function_name_equals_chartsymbol(self):
        function = Function(chartsymbol_cell)
        assert function.name == 'ChartSymbol'


class TestFunctionType(object):
    def test_function_type_equals_int(self):
        function = Function(barscalculated_cell)
        assert function.type == 'int'
    

    def test_function_type_equals_string(self):
        function = Function(chartsymbol_cell)
        assert function.type == 'string'


class TestFunctionParametersLen(object):
    def test_function_parameters_len_equals_1(self):
        function = Function(barscalculated_cell)
        assert len(function.parameters) == 1


    def test_function_parameters_len_equals_4(self):
        function = Function(objectname_cell)
        assert len(function.parameters) == 4


class TestFunctionParametersItens(object):
    def test_function_parameters_item_0_of_barscalculated(self):
        function = Function(barscalculated_cell)
        parameter = Parameter('indicator_handle', 'int')
        assert function.parameters[0] == parameter


    def test_function_parameters_item_0_of_objectname(self):
        function = Function(objectname_cell)
        parameter = Parameter('chart_id', 'long')
        assert function.parameters[0] == parameter


    def test_function_parameters_item_1_of_objectname(self):
        function = Function(objectname_cell)
        parameter = Parameter('pos', 'int')
        assert function.parameters[1] == parameter


    def test_function_parameters_item_2_of_objectname(self):
        function = Function(objectname_cell)
        parameter = Parameter('sub_window=-1', 'int')
        assert function.parameters[2] == parameter


    def test_function_parameters_item_3_of_objectname(self):
        function = Function(objectname_cell)
        parameter = Parameter('type=-1', 'int')
        assert function.parameters[3] == parameter


class TestSnippetPrefix(object):
    def test_snippet_prefix_equals_barscalculated(self):
        snippet = Function(barscalculated_cell).to_snippet()
        assert snippet['prefix'] == 'BarsCalculated()'


    def test_snippet_prefix_equals_chartsymbol(self):
        snippet = Function(chartsymbol_cell).to_snippet()
        assert snippet['prefix'] == 'ChartSymbol()'


    def test_snippet_prefix_equals_objectname(self):
        snippet = Function(objectname_cell).to_snippet()
        assert snippet['prefix'] == 'ObjectName()'


class TestSnippetBody(object):
    def test_snippet_body_of_barscalculated(self):
        snippet = Function(barscalculated_cell).to_snippet()
        assert snippet['body'] == "BarsCalculated(${1:int indicator_handle})$0"


    def test_snippet_body_of_chartsymbol(self):
        snippet = Function(chartsymbol_cell).to_snippet()
        assert snippet['body'] == "ChartSymbol(${1:long chart_id=0})$0"


class TestSnippetDescription(object):
    def test_snippet_description_of_barscalculated(self):
        snippet = Function(barscalculated_cell).to_snippet()
        assert snippet['description'] == "BarsCalculated() function"


    def test_snippet_description_of_chartsymbol(self):
        snippet = Function(chartsymbol_cell).to_snippet()
        assert snippet['description'] == "ChartSymbol() function"


    def test_snippet_description_of_objectname(self):
        snippet = Function(objectname_cell).to_snippet()
        assert snippet['description'] == "ObjectName() function"

