from setuptools import setup, find_packages

packages = find_packages(
    where='.',
    include=['compare_photos_app*']
)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="compare_photos_app",
    version="0.0.1",
    author="Jitesh Gosar",
    author_email="gosar95@gmail.com",
    description="Streamlit app to compare photos from different directories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jitesh17/compare_photos_app",
    py_modules=["compare_photos_app"],
    packages=packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[

    ],
    python_requires='>=3.6',
)
