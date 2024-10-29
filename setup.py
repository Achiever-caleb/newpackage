from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['test*']),
    license='MIT',
    description='EDSA learning python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Achiever-caleb/newpackage',
    author='Caleb',
    author_email='okoncaleb07@gmail.com'
)