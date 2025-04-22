from html.parser import HTMLParser

class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchors = {}
        self.current_href = None
        self.current_data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            attrs_dict = dict(attrs)
            self.current_href = attrs_dict.get('href')
            self.current_data = []

    def handle_data(self, data):
        if self.current_href is not None:
            self.current_data.append(data.strip())

    def handle_endtag(self, tag):
        if tag == 'a' and self.current_href:
            text = ' '.join(self.current_data).strip()
            if text:
                self.anchors.setdefault(text, []).append(self.current_href)
            self.current_href = None
            self.current_data = []

# Read the HTML content from file
with open("contemplate_his_majestic_personhood.html", encoding='utf-8') as file:
    html = file.read()

# Parse the HTML content
parser = AnchorParser()
parser.feed(html)

# Print the extracted anchor text and associated links
for text, hrefs in parser.anchors.items():
    print(f"{text} => {hrefs}")
