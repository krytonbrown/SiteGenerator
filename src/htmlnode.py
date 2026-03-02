class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def __repr__(self):
        print(f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})")

    def to_html(self):
        raise NotImplementedError("to_html is not yet implemented")
    
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        props_attrs = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return props_attrs