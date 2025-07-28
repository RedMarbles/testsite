import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
	def setUp(self):
		pass

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)

	def test_to_html_inline_array(self):
		node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
		)
		self.assertEqual(
			node.to_html(),
			'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
		)

	def test_to_html_parent_no_tag_error(self):
		node = ParentNode(None, [], {'margin': '4px'})
		self.assertRaises(ValueError, node.to_html)

	def test_to_html_parent_no_children_error(self):
		node_func = lambda : ParentNode("li", None, {'margin': '4px'})
		self.assertRaises(ValueError, node_func)

	def test_to_html_parent_empty_children(self):
		node = ParentNode("li", [])
		self.assertEqual(node.to_html(), "<li></li>")


if __name__ == "__main__":
	unittest.main()