import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='deepcohort',
     version='0.1',
     scripts=['deepcohort'] ,
     author="Lakshya Khandelwal",
     author_email="lakshaya.khandelwal@gmail.com",
     description="Cohort formation based on Automated Data Slicing",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/lakshyakh93/deepslice",
     packages=setuptools.find_packages(),
     install_requires=['pandas', 'sklearn', 'matplotlib'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )

