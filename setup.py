from setuptools import setup, find_packages
with open('README.md', 'r', encoding = 'utf-8') as f:
    long_description = f.read()
setup(
    name = 'Tavin',
    version = '1.1.8',
    description = 'A concise application framework.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/lemonorangeapple/Tavin',
    author = 'lemonorangeapple',
    author_email = 'jcj1947725596@hotmail.com',
    license = 'MIT',
    keywords = 'web framework',
    packages = find_packages(),
    install_requires = ['flask', 'pywebview'],
    python_requires = '>=3',
)