from setuptools import setup, find_packages
import bobert

setup(
    name='bobert',
    version=str(sotawhat.__VERSION__),
    packages=find_packages(),
    description='arxiv-sanity query script',
    long_description=str('Bobert is a script to query Arxiv for the latest '
                         'abstracts and extract summaries from them. '),
    url='github.com/hxjovi/bobert-tool',
    license="",
    install_requires=['six', 'nltk', 'pyspellchecker'],
    entry_points={
        'console_scripts': ['bobert=bobert.bobert:main'],
    }
)
