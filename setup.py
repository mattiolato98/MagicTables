from setuptools import setup

with open('README.rst') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name = 'django-magic-tables',
    version = '0.1.1',
    description = 'A Django app to turn easily QuerySets into tables',
    long_description_content_type= 'text/markdown',
    long_description = README,
    url = 'https://www.example.com/',
    author = 'Gabriele Mattioli',
    author_email = 'gabrymattioli@gmail.com',
    license = 'BSD-3-Clause', 
    keywords= ['Table', 'Magictable'],
    download_url='https://pypi.org/project/django-magic-tables/0.1/',
)

if __name__ == "__main__":
    setup(**setup_args)

