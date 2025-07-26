
class HTMLNode:
	def __init__(self, tag: str=None, value: str=None, children: list['HTMLNode']=None, props: dict[str, str]=None):
		self.tag = tag # if tag is None, render as raw text
		self.value = value
		self.children = children
		self.props = props
		if self.value is None and self.children is None:
			raise ValueError("HTMLNode cannot have both value and children simultaneously be None")

	def to_html(self) -> str:
		raise NotImplementedError("to_html() method not implemented")

	def props_to_html(self) -> str:
		if self.props is None:
			return ""
		res = ""
		for key, value in self.props.items():
			res += f' {key}="{value}"'
		return res

	def __repr__(self) -> str:
		tag, value, children, props = self.tag, self.value, self.children, self.props
		if children is not None:
			children = "[" + ", ".join([repr(c) for c in children]) + "]"
		return f"HTMLNode({tag=}, {value=}, {children=}, {props=})"
