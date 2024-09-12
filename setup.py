from setuptools import setup, find_packages

with open("READMEL.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name= "image_processing",
    version= "0.0.1",
    author= "Thiago Ferrari",
    author_email= "engthiagoferrari@gmail.com",
    description= "modules for transforming images and its colors through a histogram reference", 
    long_description= page_description,
    long_description_content_type= "text/markdown",
    url= "https://github.com/EngThiagoFerrari/image-processing-package.git", #inserir meu github
    packages= find_packages(),
    install_requires= requirements,
    python_requires= '>=3.10',
)