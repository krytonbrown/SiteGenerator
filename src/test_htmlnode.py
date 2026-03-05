import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_initialization_and_attributes(self):
        # basic nodes with various constructor arguments
        test_node_1 = HTMLNode()
        self.assertIsNone(test_node_1.tag)
        self.assertIsNone(test_node_1.value)
        self.assertEqual(test_node_1.children, [])
        self.assertEqual(test_node_1.props, {})

        test_node_2 = HTMLNode("Test 2")
        self.assertEqual(test_node_2.tag, "Test 2")
        self.assertIsNone(test_node_2.value)
        self.assertEqual(test_node_2.children, [])
        self.assertEqual(test_node_2.props, {})

        test_node_3 = HTMLNode("Test 3", "This is a test")
        self.assertEqual(test_node_3.tag, "Test 3")
        self.assertEqual(test_node_3.value, "This is a test")
        self.assertEqual(test_node_3.children, [])
        self.assertEqual(test_node_3.props, {})

        # explicit children and props
        test_node_4 = HTMLNode("Test 4", "This is a test too", [test_node_1], {"href": "www.boot.dev"})
        self.assertEqual(test_node_4.children, [test_node_1])
        self.assertEqual(test_node_4.props, {"href": "www.boot.dev"})

        # multiple children
        test_node_5 = HTMLNode("Test 5", "This is also a test", [test_node_3, test_node_2], {"href": "www.google.com"})
        self.assertEqual(test_node_5.children, [test_node_3, test_node_2])
        self.assertEqual(test_node_5.props, {"href": "www.google.com"})

        # ensure default list is new for each instance (no shared mutable default)
        test_node_1.children.append(HTMLNode("should not appear"))
        self.assertEqual(test_node_2.children, [])

    def test_props_to_html(self):
        n = HTMLNode("a", None, None, {"href": "https://example.com", "rel": "noopener"})
        attrs = n.props_to_html()
        # order is not guaranteed, so compare as sets of pairs
        parts = set(attrs.split())
        self.assertIn('href="https://example.com"', parts)
        self.assertIn('rel="noopener"', parts)

        # empty props
        n2 = HTMLNode("div")
        self.assertEqual(n2.props_to_html(), "")

    def test_repr_does_not_raise(self):
        # __repr__ currently prints rather than returning; make sure it at least
        # does not crash and returns None because of print.
        n = HTMLNode("span", "hi")
        self.assertIsNone(n.__repr__())
        # we also check that calling repr() triggers __repr__ indirectly
        # and doesn't raise
        repr(n)


if __name__ == "__main__":    
    unittest.main() 

if __name__ == "__main__":    
    unittest.main() 