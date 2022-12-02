```
source .venv/bin/activate
export FLASK_APP="application.py"
flask run
```

curl -i -H "Content-Type: application/json" -X POST -d '{"message":"feyza"}' http://localhost:5000/messages
echo -n "feyza" | shasum -a 256