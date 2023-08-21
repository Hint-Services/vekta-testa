from setuptools import setup, find_packages

setup(
    name="vecta-testa",
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
    ],
    author="Hint Services",
    author_email="ben@hint.services",
    description="A package for testing vector embeddings.",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Hint-Services/vekta-testa",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
