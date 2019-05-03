# !/bin/bash
mkdir -p {docs,src}
pyenv local 3.7.0
pip install -r requirement.txt
cd docs/
sphinx-quickstart
# > Separate source and build directories (y/n) [n]:
# > Project name: sphinx-autodoc-example
# > Author name(s): DanielPei
# > Project release []: 0.0.1
# > Project language [en]:

# add 'sphinx.ext.autodoc' to extensions in conf.py