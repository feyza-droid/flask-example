```
source .venv/bin/activate
export FLASK_APP="application.py"
flask run
```

```
echo -n "feyza" | shasum -a 256

curl -X POST -H "Content-Type: application/json" -d '{ "message":"<your_message>"}' http://flaskexample-env.eba-fisvhbir.us-east-1.elasticbeanstalk.com/messages
curl -X GET "http://flaskexample-env.eba-fisvhbir.us-east-1.elasticbeanstalk.com/messages?hash=<your_hash>"

Example:
curl -X POST -H "Content-Type: application/json" -d '{ "message":"feyza"}' http://flaskexample-env.eba-fisvhbir.us-east-1.elasticbeanstalk.com/messages
curl -X GET "http://flaskexample-env.eba-fisvhbir.us-east-1.elasticbeanstalk.com/messages?hash=6e8c90bed1ab401092001331be8803c89c5ca2d0283b7d8cbbb5dc19bf483cef"
```