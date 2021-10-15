from setuptools import setup

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = "src", 
    version="0.0.1",
    author ="sushantsur23",
    description="A small package for dl pipeline",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/sushantsur23/dvc_tensorflow.git",
    author_email="sushant.sur23@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires= [
        "dvc",
        "tensorflow",
        "pandas",
        "numpy",
        "matplotlib",
        "PyYAML",
        "boto3",
        "tqdm"
    ]
) 