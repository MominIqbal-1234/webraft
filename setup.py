from setuptools import setup, find_packages



VERSION = '0.5'
DESCRIPTION = "WebRaft is a Python library for creating and reading JSON Web Tokens, extracting user agent information, retrieving IP data, and creating and reading API keys."


# Setting up
setup(
    name="webraft",
    version=VERSION,
    author="mominiqbal1234",
    author_email="<mominiqbal1214@gmail.com>",
    description=DESCRIPTION,
    long_description="""
    # WebRaft

    creating and reading JSON Web Tokens, extracting user agent
    information, retrieving IP data, and creating and reading API keys

    # How to install webraft

    ```python
    pip install webraft
    ```
    # Documentation
    open Github repository for the WebRaft Python library. The link is included in the package's documentation to provide
    users with access to the source code and additional information about the library.
    <br>
    https://github.com/MominIqbal-1234/webraft



    Check Our Site : https://mefiz.com/about </br>
    Developed by : Momin Iqbal

    """,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["django","djangorestframework","PyJWT","fastapi","flask","bottle",'cryptography',"user-agents","django-user-agents"],
    keywords=['webraft','WebRaft''python', 'django', 'jwt', 'jwt for django','create api key','read api key','create token','read token','user agent django','ip info python','user agent python','jwt flask','jwt bottle','jwt fastapi'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
