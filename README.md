# Portfolio

This repository contains a small static website. Automated tests can be run with [pytest](https://docs.pytest.org/).

```bash
pip install -r requirements.txt
pytest
```

The test `tests/test_html.py` ensures that each `<img>` tag in `index.html` has a non-empty `alt` attribute using BeautifulSoup.
