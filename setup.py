from setuptools import setup, find_packages

setup(
    name='textminer-pr0-Bkey',
    version='0.1.2',
    description='A simple text processing library with stopword removal and keyword extraction. - OSS과제',
    author='keily_ae_Embuth',
    author_email='2243104@donga.ac.kr',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'scikit-learn',
        'numpy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)