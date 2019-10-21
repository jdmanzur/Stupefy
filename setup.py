import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stupefy",
    version="1.0.1",
    author="Jade Manzur && Bruno Carrazza",
    description="converts Spotify playlists to YouTube playlist",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jdmanzur/Stupefy",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':[
            'stupefy = stupefy.__main__:main'
        ]
    }
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)