import setuptools
from decouple import config

with open(file="README.md", mode="r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

SRC_REPO = "cnnClassifier"
GITHUB_REPO_NAME = config("GITHUB_REPO_NAME")
GITHUB_USER_NAME = config("GITHUB_USER_NAME")
GITHUB_USER_EMAIL = config("GITHUB_USER_EMAIL")


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=GITHUB_USER_NAME,
    author_email=GITHUB_USER_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{GITHUB_USER_NAME}/{GITHUB_REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{GITHUB_USER_NAME}/{GITHUB_REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
