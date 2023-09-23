# Text Gradient

Function to generate a list of colour gradients. Designed to wrap text where each character is surrounded by formatting blocks.

All algorithm work done by https://bsouthga.dev/posts/color-gradients-with-python

## Usage

```python
from gradient import TextGradient
my_text = TextGradient("Hello World", "#000000", "#ffffff")
print(my_text)
>>> [#000000]H[/#000000][#191919]e[/#191919][#333333]l[/#333333][#4c4c4c]l[/#4c4c4c][#666666]o[/#666666][#7f7f7f] [/#7f7f7f][#999999]W[/#999999][#b2b2b2]o[/#b2b2b2][#cccccc]r[/#cccccc][#e5e5e5]l[/#e5e5e5][#ffffff]d[/#ffffff]
```
