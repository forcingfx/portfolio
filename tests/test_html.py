import os
from bs4 import BeautifulSoup


def test_img_tags_have_alt():
    index_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    for img in soup.find_all("img"):
        assert img.has_attr("alt"), f"Image tag missing alt attribute: {img}"
        assert img["alt"].strip(), f"Image tag has empty alt attribute: {img}"

