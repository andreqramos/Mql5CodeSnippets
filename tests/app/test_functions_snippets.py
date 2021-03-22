from pathlib import Path
import pytest
from src.app.functions_snippets import FunctionsSnippets


@pytest.fixture
def functions_list_html_file(tmpdir):
    html_path = tmpdir.join("BarsCalculated.html")
    html_content = """
        <html>
          <head>
          </head>
          <body>
            <H1>BarsCalculated</H1>
            <table>
              <tr class="EnumTable">
                <td class="EnumTable"><p class="p_fortable"><span class="f_fortable">Function</span></p>
                </td>
                <td class="EnumTable"><p class="p_fortable"><span class="f_fortable">Action</span></p>
                </td>
                <td class="EnumTable"><p class="p_fortable"><span class="f_fortable">Section</span></p>
                </td>
              </tr>
              <tr class="EnumTable">
                <td class="EnumTable"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/account/accountinfodouble" class="topiclink">AccountInfoDouble</a></span></p>
                </td>
                <td class="EnumTable"><p class="p_fortable"><span class="f_fortable">Returns a value of double type of the corresponding account property</span></p>
                </td>
                <td class="EnumTable"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/account" class="topiclink">Account Information</a></span></p>
                </td>
              </tr>
              <tr class="EnumTable">
                <td class="EnumTable"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/account/accountinfointeger" class="topiclink">AccountInfoInteger</a></span></p>
                </td>
                <td class="EnumTable"><p class="p_fortable"><span class="f_fortable">Returns a value of integer type (bool, int or long) of the corresponding account property</span></p>
                </td>
                <td class="EnumTable"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/account" class="topiclink">Account Information</a></span></p>
                </td>
              <tr class="EnumTable">
                <td class="EnumTable"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/common/zeromemory" class="topiclink">ZeroMemory</a></span></p>
                </td>
                <td class="EnumTable"><p class="p_fortable"><span class="f_fortable">Resets a variable passed to it by reference. The variable can be of any type, except for classes and structures that have constructors.</span></p>
                </td>
                <td class="EnumTable"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/common" class="topiclink">Common Functions</a></span></p>
                </td>
              </tr>
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


class TestFunctionsSnippetsHtml(object):
    def test_html_attribute_case_1(self, functions_list_html_file):
        functions_snippets = FunctionsSnippets(functions_list_html_file)
        assert functions_snippets.html == functions_list_html_file


class TestGetFunctionsLinks(object):

    def test_get_functions_links_first_function(self, functions_list_html_file):
        functions_snippets = FunctionsSnippets(functions_list_html_file)
        assert functions_snippets.get_functions_links()[0] == 'https://www.mql5.com/en/docs/account/accountinfodouble'


    def test_get_functions_links_second_function(self, functions_list_html_file):
        functions_snippets = FunctionsSnippets(functions_list_html_file)
        assert functions_snippets.get_functions_links()[1] == 'https://www.mql5.com/en/docs/account/accountinfointeger'


    def test_get_functions_links_last_function(self, functions_list_html_file):
        functions_snippets = FunctionsSnippets(functions_list_html_file)
        assert functions_snippets.get_functions_links()[-1] == 'https://www.mql5.com/en/docs/common/zeromemory'


class TestFunctionsSnippetsLinks(object):

    def test_links_attribute_case_1(self, functions_list_html_file):
        functions_snippets = FunctionsSnippets(functions_list_html_file)
        assert functions_snippets.links[0] == 'https://www.mql5.com/en/docs/account/accountinfodouble'


    def test_links_attribute_case_2(self, functions_list_html_file):
        functions_snippets = FunctionsSnippets(functions_list_html_file)
        assert functions_snippets.links[1] == 'https://www.mql5.com/en/docs/account/accountinfointeger'


    def test_links_attribute_case_3(self, functions_list_html_file):
        functions_snippets = FunctionsSnippets(functions_list_html_file)
        assert functions_snippets.links[-1] == 'https://www.mql5.com/en/docs/common/zeromemory'

