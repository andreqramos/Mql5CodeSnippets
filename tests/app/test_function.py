from pathlib import Path
import pytest
from src.app.function import Function
from src.app.parameter import Parameter


@pytest.fixture
def barscalculated_html_file(tmpdir):
    html_path = tmpdir.join("BarsCalculated.html")
    html_content = """
        <html>
          <head>
          </head>
          <body>
            <H1>BarsCalculated</H1>
            <table>
              <tr>
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
                </td>
              </tr>
            </table>
            <table>
            </table>
          </body>
        </html>
    """
    with Path(html_path).open(mode='w+') as f:
        f.write(html_content)
    yield html_path


@pytest.fixture
def chartsymbol_html_file(tmpdir):
    html_path = tmpdir.join("BarsCalculated.html")
    html_content = """
        <html>
          <head>
          </head>
          <body>
            <H1>BarsCalculated</H1>
            <table>
              <tr>
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
                </td>
              </tr>
            </table>
            <table>
            </table>
          </body>
        </html>
    """
    with Path(html_path).open(mode='w+') as f:
        f.write(html_content)
    yield html_path


@pytest.fixture
def objectname_html_file(tmpdir):
    html_path = tmpdir.join("ObjectName.html")
    html_content = """
        <html>
          <head>
          </head>
          <body>
            <H1>ObjectName</H1>
            <table>
              <tr>
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
                </td>
              </tr>
            </table>
            <table>
            </table>
          </body>
        </html>
    """
    with Path(html_path).open(mode='w+') as f:
        f.write(html_content)
    yield html_path


class TestFunctionName(object):
    def test_function_name_equals_barscalculated(self, barscalculated_html_file):
        function = Function(barscalculated_html_file)
        assert function.name == 'BarsCalculated'


    def test_function_name_equals_chartsymbol(self, chartsymbol_html_file):
        function = Function(chartsymbol_html_file)
        assert function.name == 'ChartSymbol'


class TestFunctionType(object):
    def test_function_type_equals_int(self, barscalculated_html_file):
        function = Function(barscalculated_html_file)
        assert function.type == 'int'
    

    def test_function_type_equals_string(self, chartsymbol_html_file):
        function = Function(chartsymbol_html_file)
        assert function.type == 'string'


class TestFunctionParametersLen(object):
    def test_function_parameters_len_equals_1(self, barscalculated_html_file):
        function = Function(barscalculated_html_file)
        assert len(function.parameters) == 1


    def test_function_parameters_len_equals_4(self, objectname_html_file):
        function = Function(objectname_html_file)
        assert len(function.parameters) == 4


class TestFunctionParametersItens(object):
    def test_function_parameters_item_0_of_barscalculated(self, barscalculated_html_file):
        function = Function(barscalculated_html_file)
        parameter = Parameter('indicator_handle', 'int')
        assert function.parameters[0] == parameter


    def test_function_parameters_item_0_of_objectname(self, objectname_html_file):
        function = Function(objectname_html_file)
        parameter = Parameter('chart_id', 'long')
        assert function.parameters[0] == parameter


    def test_function_parameters_item_1_of_objectname(self, objectname_html_file):
        function = Function(objectname_html_file)
        parameter = Parameter('pos', 'int')
        assert function.parameters[1] == parameter


    def test_function_parameters_item_2_of_objectname(self, objectname_html_file):
        function = Function(objectname_html_file)
        parameter = Parameter('sub_window=-1', 'int')
        assert function.parameters[2] == parameter


    def test_function_parameters_item_3_of_objectname(self, objectname_html_file):
        function = Function(objectname_html_file)
        parameter = Parameter('type=-1', 'int')
        assert function.parameters[3] == parameter


class TestSnippetPrefix(object):
    def test_snippet_prefix_equals_barscalculated(self, barscalculated_html_file):
        snippet = Function(barscalculated_html_file).to_snippet()
        assert snippet['prefix'] == 'BarsCalculated()'


    def test_snippet_prefix_equals_chartsymbol(self, chartsymbol_html_file):
        snippet = Function(chartsymbol_html_file).to_snippet()
        assert snippet['prefix'] == 'ChartSymbol()'


    def test_snippet_prefix_equals_objectname(self, objectname_html_file):
        snippet = Function(objectname_html_file).to_snippet()
        assert snippet['prefix'] == 'ObjectName()'


class TestSnippetBody(object):
    def test_snippet_body_of_barscalculated(self, barscalculated_html_file):
        snippet = Function(barscalculated_html_file).to_snippet()
        assert snippet['body'] == ["BarsCalculated(${1:int indicator_handle})$0"]


    def test_snippet_body_of_chartsymbol(self, chartsymbol_html_file):
        snippet = Function(chartsymbol_html_file).to_snippet()
        assert snippet['body'] == ["ChartSymbol(${1:long chart_id=0})$0"]


class TestSnippetDescription(object):
    def test_snippet_description_of_barscalculated(self, barscalculated_html_file):
        snippet = Function(barscalculated_html_file).to_snippet()
        assert snippet['description'] == "BarsCalculated() function"


    def test_snippet_description_of_chartsymbol(self, chartsymbol_html_file):
        snippet = Function(chartsymbol_html_file).to_snippet()
        assert snippet['description'] == "ChartSymbol() function"


    def test_snippet_description_of_objectname(self, objectname_html_file):
        snippet = Function(objectname_html_file).to_snippet()
        assert snippet['description'] == "ObjectName() function"

