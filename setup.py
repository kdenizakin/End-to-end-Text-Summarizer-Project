import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-end-Text-Summarizer-Project"
AUTHOR_USER_NAME = "kdenizakin"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "korhandenizakin@gmail.com"

setuptools.setup( #This setup function will look for all of the constructor files and install them. 
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_USER_NAME,
    description="My Text Summarizer Project for The Deep Learning Course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kdenizakin/End-to-end-Text-Summarizer-Project",
    project_urls={
        "Bug Tracker": "https://github.com/kdenizakin/End-to-end-Text-Summarizer-Project/issues",
        "Source Code": "https://github.com/kdenizakin/End-to-end-Text-Summarizer-Project",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"]
)