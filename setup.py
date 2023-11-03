from setuptools import setup, find_packages

setup(
    name='python_sqlite_library',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple SQLite library for Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/python_sqlite_library',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # 'example-package>=1.2.3', # Uncomment and replace with actual dependencies if needed
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    },
)