from distutils.core import setup

setup(
    name='ReverseEngineeringTools',
    version='0.1.0',
    author='Will Oursler',
    author_email='woursler@gmail.com',
    packages=['retools'],
    scripts=[],#['bin/wash-towels.py'],
    url='http://pypi.python.org/pypi/reverseengineeringtools/',
    license='LICENSE.txt',
    description='A suite of reverse engineering tools.',
    long_description=open('README.txt').read(),
    install_requires=[
	"SVGFig == 1.1.6",
	"pydot >= 1.0.28",
    ],
)
