echo "Build Start Temirlan"
# build_files.sh
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear

echo "Build End Temirlan"