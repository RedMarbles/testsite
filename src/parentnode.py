from htmlnode import HTMLNode

class ParentNode(HTMLNode):
	def __init__(self, tag: str, children: list['HTMLNode'], props: dict[str, str]=None):
		super().__init__(tag, value=None, children=children, props=props)
	
	def to_html(self) -> str:
		if self.tag is None:
			raise ValueError("ParentNode needs to have a valid 'tag' field")
		if self.children is None:
			raise ValueError("ParentNode needs to have child nodes")
		child_strs = (child.to_html() for child in self.children)
		child_str = "".join(child_strs)
		return f"<{self.tag}{self.props_to_html()}>{child_str}</{self.tag}>"

	def __repr__(self) -> str:
		tag, children, props = self.tag, self.children, self.props
		return f'ParentNode({tag=}, {children=}, {props=})'
