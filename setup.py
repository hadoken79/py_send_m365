import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='py_send_m365',
    version='0.1.5',
    author='hadoken',
    author_email='hadoken79@protonmail.com',
    description='A simple library to send email from an existing M365 account in Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/hadoken79/py_send_m365',
    project_urls={
        "Bug Tracker": "https://github.com/hadoken79/py_send_m365/issues"
    },
    license='MIT',
    packages=['py_send_m365'],
    install_requires=[],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="email M365 Microsoft SMTP Python",
)
