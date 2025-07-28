from htmlnode import HTMLNode

class LeafNode(HTMLNode):
	def __init__(self, tag: str, value: str, props: dict[str, str]=None):
		super().__init__(tag, value, children=None, props=props)
	
	def to_html(self) -> str:
		if self.value is None or self.value == "":
			raise ValueError("LeafNode needs to have a valid 'value' field")
		if self.tag is None:
			return self.value
		return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

	def __repr__(self) -> str:
		tag, value, props = self.tag, self.value, self.props
		return f'LeafNode({tag=}, {value=}, {props=})'
