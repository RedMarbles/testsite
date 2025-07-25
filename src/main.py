from textnode import TextNode, TextType

def main():
	text = TextNode("This is some anchor text", TextType.TEXT_LINK, "https://www.boot.dev")
	print(text)
	text2 = TextNode("This is some anchor text", TextType.TEXT_ITALIC)
	print(text2)
	print(text == text2)

if __name__ == "__main__":
	main()
