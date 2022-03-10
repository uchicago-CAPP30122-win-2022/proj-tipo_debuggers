echo -e "1. Creating new virtual environment..."
python -m venv env 

echo -e "2. Installing Requirements..."

source env/bin/activate
pip install -r requirements.txt
python crimes_main.py

deactivate
rm -r env
echo -e "Bye bye! :D"