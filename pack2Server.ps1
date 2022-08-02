Remove-Item -recurse build
Remove-Item -recurse *.egg-info
Remove-Item -recurse dist
python setup.py sdist bdist_wheel
twine upload -r nexus dist/*