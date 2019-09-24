#! /usr/bin/python



from setuptools import setup, find_packages



setup(

    name='Motor',

    version='1.0.0',

    description='Python code to control a MG90S servo on a Raspberry Pi',

    url='https://github.com/tuj05689/Pi-MG90S-Motor',

    author='Adam Pienkowski',

    author_email='tuj05689@temple.edu',

    packages=find_packages(),

    install_requires=['gpiozero','time']

    )
