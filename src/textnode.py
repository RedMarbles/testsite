from enum import Enum

class TextType(Enum):
	TEXT = "TEXT"
	BOLD = "BOLD"
	ITALIC = "ITALIC"
	CODE = "CODE"
	LINK = "LINK"
	IMAGE = "IMG"

class TextNode:
	def __init__(self, text: str, text_type: TextType, url: str=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other: 'TextNode') -> bool:
		check = self.text == other.text
		check &= self.text_type == other.text_type
		check &= self.url == other.url
		return check

	def __repr__(self) -> str:
		text, text_type, url = self.text, self.text_type.value, self.url
		return f"TextNode({text=}, {text_type=}, {url=})"
