import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="titleize",
    version="0.0.3",
    author="Tabulate",
    author_email="tabulatejarl8@gmail.com",
    description="Convert Strings to Title Case",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TabulateJarl8/titleize",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
	install_requires=[
		"nltk"
	],
)
