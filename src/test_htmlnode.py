import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_html(self):
        test_node_1 = HTMLNode()
        test_node_2 = HTMLNode("Test 2")
        test_node_3 = HTMLNode("Test 3", "This is a test")
        test_node_4 = HTMLNode("Test 4", "This is a test too", [test_node_1], {"href": "www.boot.dev"})
        test_node_5 = HTMLNode("Test 5", "This is also a test", [test_node_3, test_node_2], {"href": "www.google.com"})


if __name__ == "__main__":
    unittest.main()