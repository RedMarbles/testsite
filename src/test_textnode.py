import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
	def test_eq_bold(self):
		node1 = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node1, node2)

	def test_eq_link(self):
		node1 = TextNode("This is a link", TextType.LINK, "https:\\www.google.com")
		node2 = TextNode("This is a link", TextType.LINK, "https:\\www.google.com")
		self.assertEqual(node1, node2)

	def test_eq_false(self):
		node1 = TextNode("This is a text node", TextType.TEXT)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node1, node2)

	def test_eq_false2(self):
		node1 = TextNode("This is a text node", TextType.TEXT)
		node2 = TextNode("This is a text node2", TextType.TEXT)
		self.assertNotEqual(node1, node2)

	def test_eq_false3(self):
		node1 = TextNode("This is a link", TextType.LINK, "https:\\www.google.com")
		node2 = TextNode("This is a link", TextType.LINK, "https:\\www.gooogle.com")
		self.assertNotEqual(node1, node2)

	def test_repr(self):
		node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
		self.assertEqual(
			"TextNode(text='This is a text node', text_type='TEXT', url='https://www.boot.dev')", repr(node)
		)


if __name__ == "__main__":
	unittest.main()
