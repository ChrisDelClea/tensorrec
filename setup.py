from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

setup(
  name='tensorrec',
  packages=['tensorrec'],
  version='2.26.2',
  description='A TensorFlow recommendation algorithm and framework in Python.',
  author='',
  author_email='',
  url='https://github.com/jfkirk/tensorrec',
  keywords=['machine-learning', 'tensorflow', 'recommendation-system', 'python', 'recommender-system', 'tensorflow 2'],
  classifiers=[],
  install_requires=[
      "numpy>=1.14.1",
      "scipy>=0.19.1",
      "six>=1.11.0",
      "tensorflow==2.3.1",
  ],
)
