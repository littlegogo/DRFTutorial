# coding:utf-8
from setuptools import setup, find_packages


setup(
    name='tutorial',
    version='0.1',
    description='django restframework demo',
    author='mangogo',
    author_email='youremail@gmail.com',
    url='https://www.xxx.com',
    license='MIT',
    packages=find_packages('tutorial'),
    package_dir={'': 'tutorial'},
    include_package_data=True,
    install_requires=[
        'django>=2.0',
    ],
    scripts=[
        'tutorial/manage.py',
        'tutorial/tutorial/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'tutorial_manage = manage:main',
        ]
    },
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: DRF :: Django DRF demo',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],

)
