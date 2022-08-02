rm -r build
rm -r *.egg-info
rm -r dist
python setup.py sdist bdist_wheel
pip install .
echo "Successfully installed"
python -c "import camel_k8s_config"
echo "Successfully imported"
twine upload -r nexus dist/*