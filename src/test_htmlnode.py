import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<p>", 
                        "hello world", 
                        children = None, 
                        props = {
                                "href": "https://www.seznam.cz",
                                "target": "_blank",
                                }
                )
        node2 = HTMLNode("<p>", 
                        "hello world", 
                        children = None, 
                        props = {
                                "href": "https://www.seznam.cz",
                                "target": "_blank",
                                }
                )
        print(node.props_to_html())

if __name__ == "__main__":
    unittest.main()