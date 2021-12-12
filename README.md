# AD - Homework

To run the application Locally:
```
cd <project_folder>
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 autodesk_homework.py
```

Docker Build steps:
```
cd <path/to/repo>

docker build -t ad-homework:latest .

docker run -d -p 5000:5000 ad-homework
```

To view logs in Docker:
```
docker exec -it <container> bash
tail -f request.log
```

To Enable Logging output to file(Debug Mode):
```
Edit line 2 of config.json
Set "DEBUG": 1
To disable, set to 0.
```

An example request that can be used to test from command line:
```
curl -X GET http://127.0.0.1:5000/
```
