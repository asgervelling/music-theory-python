# music-theory-python


Run debug environment with hot reloading:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```

Build and run in a container: `docker-compose up --build`

Server is now running on localhost:5000

```
curl http://127.0.0.1:5000/chords/Dmaj9/degrees
>>> ["1", "3", "5", "Δ", "9"]

curl http://127.0.0.1:5000/chords/Dmaj9/midi
>>> [62, 66, 69, 73, 76]
```
