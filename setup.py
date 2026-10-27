from setuptools import setup

setup(
    name="mkdocs-readme-titles",
    version="0.1.0",
    py_modules=["readme_titles"],
    entry_points={
        "mkdocs.plugins": [
            "readme-titles = readme_titles:ReadmeTitlesPlugin",
        ]
    },
)
