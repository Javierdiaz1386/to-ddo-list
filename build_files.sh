# build_files.sh
echo "Build Start"
pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
echo "Build End"