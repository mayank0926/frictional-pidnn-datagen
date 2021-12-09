from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
      long_description = fh.read()

setup(name='frictional_pidnn_datagen',
      version='0.0.1',
      author='Mayank Yadav',
      author_email='yadav.mayank2000@gmail.com',
      description='Data genration for frictional PIDNN through MuJoCo',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/mayank0926/frictional-pidnn-datagen',
      license='BSD 3',
      packages=['frictional_pidnn_datagen'],
      install_requires=['gym'],
)
