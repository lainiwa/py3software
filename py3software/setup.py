import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='py3software',
    version='0.0.1',
    author='Lain Iwakura',
    author_email='dev_null@dontwritehere.com',
    maintainer='Lain Iwakura',
    maintainer_email='dev_null@dontwritehere.com',
    description='Face-Six Agent',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/lainiwa/py3software',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'opencv-contrib-python-headless',
        'face_recognition',
        'requests',
        'requests_toolbelt',
        'flask',
        'youtube_dl',
        'ipython',
        'colored_traceback',
        'pyyaml',
        'colour',
        'imutils',
        'dpath',
        'funcy',
    ],
    entry_points={
        'console_scripts': [
            'sayhello=py3software.main:main',
        ],
    }
)
