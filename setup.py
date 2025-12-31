from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_packages(file_path:str) -> List[str]:
    """This function returns list of requirements
    """
    requirements = []
    with open(file_path) as file:
        requirements=file.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="ML_Project",
    version="0.0.1",
    author="Ashu",
    author_email="ashufrancis673@gmail.com",
    packages= find_packages(),
    install_requires=get_packages('requirements.txt'),
    python_requires = ">=3.7"
)

