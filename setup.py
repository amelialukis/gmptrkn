import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gmptrkn",
    version="0.0.1",
    author="Amelia Lukis",
    author_email="amelialukis01@gmail.com",
    description="fetch the latest earthquake information from BMKG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amelialukis/gmptrkn",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
