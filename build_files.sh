echo "Build Start Temirlan"
# build_files.sh
sudo apt-get install python-sqlite
pip install -r requirements.txt
# python3.9 manage.py collectstatic --noinput --clear
python3.9 manage.py runserver

echo "Build End Temirlan"