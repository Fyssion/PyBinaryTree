import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyBinaryTree",
    version="0.0.1",
    author="Fyssion",
    author_email="incompetentanimator@gmail.com",
    description="Personal project to learn how binary trees work.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fyssion/PyBinaryTree",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)