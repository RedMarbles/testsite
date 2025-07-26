import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
	def test_to_html(self):
		node = HTMLNode("p", "This is a text node")
		self.assertRaises(NotImplementedError, node.to_html)

	def test_props_to_html(self):
		node1 = HTMLNode("p", "This is a text node", props={"color": "#ff3625", "font-family": "arial"})
		self.assertEqual(node1.props_to_html(), ' color="#ff3625" font-family="arial"')
		node2 = HTMLNode("p", "This is a text node")
		self.assertEqual(node2.props_to_html(), '')

	def test_repr(self):
		self.maxDiff = None
		node1 = HTMLNode("i", "italicized text", props={"color": "#ff3625", "font-family": "arial"})
		self.assertEqual(
			"HTMLNode(tag='i', value='italicized text', children=None, props={'color': '#ff3625', 'font-family': 'arial'})", 
			repr(node1),
		)
		node2 = HTMLNode("p", "This is a block that has inline spans", [node1, node1])
		self.assertEqual(
			"HTMLNode(tag='p', value='This is a block that has inline spans', children=\"[" + repr(node1) + ", " + repr(node1) + "]\", props=None)", 
			repr(node2)
		)


if __name__ == "__main__":
	unittest.main()
