import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pytex',
    version='0.0.8',
    author='Chengzhang Zhu',
    author_email='kevin.zhu.china@gmail.com',
    description='PyTex: Latex tools for easy manuscript writing.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chengzhangzhu/pytex",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'pandas'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
