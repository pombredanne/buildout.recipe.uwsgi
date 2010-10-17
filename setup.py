from setuptools import setup, find_packages

setup(
    name='shaunsephton.recipe.uwsgi',
    version='0.0.1',
    description='Buildout recipe downloading, compiling and configuring python paths for uwsgi.',
    long_description = open('README.rst', 'r').read(),
    author='Shaun Sephton',
    author_email='shaunsephton@gmail.com',
    license='BSD',
    url='http://github.com/shaunsephton/shaunsephton.recipe.uwsgi',
    packages = find_packages(),
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)