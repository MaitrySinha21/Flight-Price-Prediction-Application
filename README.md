### Flight-Price-Prediction
### It is a Machine Learning model application which is trained using Xgboost algorithm and Implemented on Flask using Opencv,HTML and deployed on Heroku...


![Flight1](https://user-images.githubusercontent.com/52413661/120456651-7128e580-c3b3-11eb-9dd3-5ac9fc3a7f2d.PNG)
### This is the main page the first page where we need to choose the details of our required flight to predict the price..
![Flight2](https://user-images.githubusercontent.com/52413661/120456662-74bc6c80-c3b3-11eb-9b18-d91037a779d1.PNG)
### Now, after choosing the details we will get the second page where it will show us the predicted price..


### Here is deployment link on Heroku :--  

https://flightprice-prediction-app.herokuapp.com/

### The dependencies/libraries are:

appdirs==1.4.3
certifi==2020.6.20
click==7.1.2
distlib==0.3.0
Flask==1.1.2
Flask-Cors==3.0.8
gunicorn==20.0.4
itsdangerous==1.1.0
Jinja2==2.11.2
joblib==0.15.1
MarkupSafe==1.1.1
numpy==1.18.1
pandas==1.0.1
python-dateutil==2.8.1
pytz==2019.3
scikit-learn==0.22.1
scipy==1.4.1
six==1.14.0
virtualenv==20.0.7
Werkzeug==1.0.1
wincertstore==0.2

### You can find this dependencies from requirements.txt file..

# How to run on local machine:

1) After clonning you have to open it on pycharm or have to open your Anaconda prompt..
2) Then create a virtual enviorment with python 3.6.12 . Command to create is---> 
     ### conda create -n venv python==3.6.12 ( on anaconda prompt)..
3) Now after creating & activating virtual enviorment install requirements.txt.. Command is--> 
     ### pip install -r requrements.txt
4) Run app.py
