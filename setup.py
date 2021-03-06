from setuptools import setup
from Prediction import __version__ as current_version

setup(
  name='bikechallenge_ng',
  version=current_version,
  description='Prediction the number of bikes crossing ',
  url='https://github.com/goujilinouhaila-coder/Bike_Challenge.git',
  author='Goujili Nouhaila',
  author_email='goujilinouhaila@gmail.com',
  license='MIT',
  packages=['Prediction','Prediction.io', 'Prediction.preprocess', 'Prediction.vis'],
  zip_safe=False
) 