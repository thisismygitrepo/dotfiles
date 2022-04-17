
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="croshell",
    version="0.0.1",
    author="Alex Al-Saffar",
    author_email="programmer@usa.com",
    description="Dotfiles management package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thisismygitrepo/dofiles",
    project_urls={
        "Bug Tracker": "https://github.com/thisismygitrepo/dofiles/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)

# python setup.py sdist bdist_wheel
# twine upload dist/*
