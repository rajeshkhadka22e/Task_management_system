// vercel_build.sh
echo "Building project packages..."
echo "Installing project requirements..."
python3.12 -m pip install -r requirements.txt

echo "Collecting static files..."
python3.12 manage.py collectstatic --noinput