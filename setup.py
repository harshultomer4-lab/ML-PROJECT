from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    ''''
    this function will return the list of requirements
    '''''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines() 
        requirements=[req.replace("\n","") for req in requirements]
        ##we have to remove the \n that gets read line by line

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
 
setup(
    name='mlproject',
    version='0.0.1',
    author='harshul',
    author_email='harshultomer4@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

) 