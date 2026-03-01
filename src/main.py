from textnode import TextNode, TextType

print("hello world")

def main():
    node1 = TextNode("Hello, World!", TextType.PLAIN, "https://www.boot.dev")
    print(node1)

main()