import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = ['Cython==3.0.3','responder','graphql-core==2.3.2','graphene==2.1.8','numpy==1.18.5','matplotlib==3.3.4','pandas==1.1.5','protobuf==3.20.2','click==7.1.2','tensorflow-cpu==2.3.1','tensorflow_hub','transformers[tf-cpu]==3.0.2','rake_nltk','nltk','cryptography','sqlalchemy_utils','sqlalchemy==1.3.24','awswrangler==1.7.0']

setuptools.setup(
    name="tableqa", # Replace with your own username
    version="0.0.1",
    author="Abhijith Neil Abraham, Fariz Rahman",
    author_email="abhijithneilabrahampk@gmail.com,farizrahman4u@gmail.com",
    description="Tool for querying natural language on tabular data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GNU GPL v2',
    url="https://github.com/abhijithneilabraham/tableQA",
    install_requires=install_requires,
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    include_package_data=True
)