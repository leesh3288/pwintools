from setuptools import setup

PKG_NAME = "PWiNTOOLS"
VERSION  = "0.4"


setup(
    name = PKG_NAME,
    version = VERSION,
    author = 'Mastho (modified by Xion)',
    author_email = 'none',
    description = 'Windows basic pwntools - exploit development library',
    license = 'MIT',
    keywords = 'windows python exploit',
    url = 'https://github.com/leesh3288/pwintools',
    py_modules=['pwintools'],
    install_requires=[
        'PythonForWindows==0.4',
        'pefile',
    ],
    dependency_links=[
        'git+git://github.com/hakril/PythonForWindows@V0.4#egg=PythonForWindows-0.4',
    ]
)