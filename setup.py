from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="shopping-cart",
    version="0.1.0",
    author="Mohamed El Wafi",
    author_email="med.wafi@gmail.com",
    description="A simple shopping cart implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/taafouch/shopping_cart",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "six>=1.16.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.3.1",
        ],
    },
)
