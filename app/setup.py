from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="banking_app",
    version="1.0.0",
    author="Abhisek Ashirbad Sethy",
    author_email="abhisek.pdev@gmail.com",
    description="A simple CLI-based banking application using Typer and SQLite",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Abhisek-Ashirbad/banking_app",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "banking-app=app:app"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12.0",
)
