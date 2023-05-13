echo "Build Start Temirlan"
# build_files.sh
<<<<<<< HEAD
pip install -r requirements.txt
# python3.9 manage.py collectstatic --noinput --clear
python3.9 manage.py runserver
=======
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
>>>>>>> parent of e2bc563 (test)

echo "Build End Temirlan"