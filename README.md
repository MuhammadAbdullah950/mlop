mkdir project1
cd project1
which python ( print environement in this case is default virtual environment)
python3 surce -m venv .venv ( create virtual environment in .venv)
cd .venv
source .venv/bin/activate
which python
touch requirement.txt ( write all packages which install)
pip freeze any_package_name
pip freeze ( list all installed package )
pip freeze > requirement.txt ( write all installed packages in requirement.txt )
pip install -r requirement.txt ( install all packages which mentioned in requirement.txt)
pytest test.py ( to run all test in test.py)
( GUI base testing is different should be explore)
