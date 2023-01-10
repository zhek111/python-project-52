from setuptools import setup, find_packages

setup(
    name='hexlet-code',
    version='0.1.0',
    description='',
    author='evgeny',
    author_email='zhek12322@gmail.com',
    url='https://github.com/zhek111/python-project-52',
    packages=find_packages(),
    install_requires=[
        'Django==4.1.4',
        'dj-database-url==0.5.0',
        'django-bootstrap4==22.3',
        'django-filter==22.1',
        'asgiref==3.5.2',
        'gunicorn==20.1.0',
        'psycopg2==2.9.5',
        'python-dotenv==0.21.0',
        'python-gettext==4.1',
        'rollbar==0.16.3',
        'sqlparse==0.4.3',
        'whitenoise==6.2.0',
    ],
    dependency_links=[]
)