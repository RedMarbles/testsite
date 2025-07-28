import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_a(self):
		node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
		self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

	def test_leaf_to_html_h2(self):
		node = LeafNode("h2", "This is a header", {"font-family": "arial", "color": "#ff3625"})
		self.assertEqual(node.to_html(), '<h2 font-family="arial" color="#ff3625">This is a header</h2>')
	
	def test_leaf_to_html_no_tag(self):
		node = LeafNode(None, "Hello, world!")
		self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
	unittest.main()