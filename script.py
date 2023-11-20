Python:


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a Flask app on AWS Elastic Beanstalk.'

if __name__ == '__main__':
    app.run()


Requirements: 


Flask==1.1.2

