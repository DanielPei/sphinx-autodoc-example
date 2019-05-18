# !/bin/python
# -*- coding:utf-8 -*-

# @Author  : Daniel.Pei
# @Email   : peixq1222@icloud.com
# @Created : 10/05/2019 22:41

from setuptools import setup, find_packages
from src.tools.version import get_setup_version

ProjectName='py_utils'
Author='DanielPei'
Email='peixq1222@icloud.com'
URL='https://github.com/DanielPei/sphinx-autodoc-example.git'
DocUrl='https://sphinx-autodoc-example.readthedocs.io/en/latest/'

setup(
    name=ProjectName,
    url=URL,
    author=Author,
    author_email=Email,
    maintainer=Author,
    maintainer_email=Email,
    version=get_setup_version(),
    description='Python 工具库',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='utils',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    python_requires='>=2.7',
    project_urls={
        'Documentation': DocUrl,
        'Source': URL,
        'Tracker': '%s/issues' % URL,
    },
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 1 - Dev',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications :: Email',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Testing :: Unit',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Utilities',
    ],
    entry_points = {
        'console_scripts' :[
            'pycmd=tools.cli:main'
        ]
    }
)