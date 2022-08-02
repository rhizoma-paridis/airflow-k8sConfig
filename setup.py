from setuptools import setup
from setuptools.config import read_configuration

setup(name='camel_k8s_config',
      version='0.0.2',
      description='build k8s config',
      author='The fastest man alive.',
      packages=['camel_k8s_config'],
      install_requires=['kubernetes'])
