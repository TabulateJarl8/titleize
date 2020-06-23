[![PyPI version](https://badge.fury.io/py/titleize.svg)](https://badge.fury.io/py/titleize)
[![Downloads](https://pepy.tech/badge/titleize)](https://pepy.tech/project/titleize)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/TabulateJarl8/titleize/graphs/commit-activity)
[![GitHub issues](https://img.shields.io/github/issues/TabulateJarl8/titleize.svg)](https://GitHub.com/TabulateJarl8/titleize/issues/)


# Titleize
----
Titleize is a Python module to convert text to Title Case. Title Case is the text format that is commonly used in titles. Example: `There Is a Bird Over There. He Is a Robin`

It may not look like much but there are specific rules to follow to make This format appealing to the himan eye, and I've compressed it down into a Python module.

----

# Usage:
Titleize is extremely simple to use. Just pass your string to the function and its done! Example:

```python
import titleize
print(titleize.titleize("i like to look at birds. Birds are really cool animals."))
```

That would output

```
I Like to Look At Birds. Birds Are Really Cool Animals.
```

Pretty cool, right? What are you waiting for? Install it now with `pip install titleize`