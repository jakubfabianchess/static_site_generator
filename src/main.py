from textnode import TextNode, TextType

def main():
    newNode = TextNode("first", TextType.LINK, "https://seznam.cz")
    print(newNode)

main()