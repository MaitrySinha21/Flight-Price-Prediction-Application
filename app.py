from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import cross_origin
import pandas as pd
import numpy as np 
import datetime 
import pickle



app = Flask(__name__)
model = pickle.load(open("flight_model.pkl", "rb"))


@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("home.html")


@app.route("/predict",methods=["GET","POST"])
@cross_origin()
def predict():
	if request.method == 'POST':
		#for stops
		TotalStop = int(request.form["stops"])
		#for time
		time = request.form["Time"]
		hr = int(pd.to_datetime(time,format="%H:%M").hour)
		mi = int(pd.to_datetime(time,format="%H:%M").minute)
		DepTime = hr + round(mi/60,2)
        #for day & Month
		data = request.form['Date']
		day = int(pd.to_datetime(data,format="%Y-%m-%dT").day)
		month = int(pd.to_datetime(data,format="%Y-%m-%dT").month)
		#making first list
		lst1 = [TotalStop,DepTime,day,month]

		#for Source
		source = request.form['source']
		if source == 'Bangalore':
			FromCity = [0,0,0,0]
		if source == 'Chennai':
			FromCity = [1,0,0,0]
		if source == 'Delhi':
			FromCity = [0,1,0,0]
		if source == 'Kolkata':
			FromCity = [0,0,1,0]
		if source == 'Mumbai':
			FromCity = [0,0,0,1]

		#for Destination
		destination = request.form['destination']
		if destination == 'Bangalore':
			ToCity = [0,0,0,0,0]
		if destination == 'Cochin':
			ToCity = [1,0,0,0,0]
		if destination == 'Delhi':
			ToCity = [0,1,0,0,0]
		if destination == 'Hydrabad':
			ToCity = [0,0,1,0,0]
		if destination == 'Kolkata':
			ToCity = [0,0,0,1,0]

		#for Airline
		airline = request.form['airline']
		if airline == 'Air Asia':
			Airline = [0,0,0,0,0,0,0,0,0,0,0]
		if airline == 'Air India':
			Airline = [1,0,0,0,0,0,0,0,0,0,0]
		if airline == 'Go Air':
			Airline = [0,1,0,0,0,0,0,0,0,0,0]
		if airline == 'Indigo':
			Airline = [0,0,1,0,0,0,0,0,0,0,0]
		if airline == 'Jet Air':
			Airline = [0,0,0,1,0,0,0,0,0,0,0]
		if airline == 'Jet Air Business Eco':
			Airline = [0,0,0,0,1,0,0,0,0,0,0]
		if airline == 'Multi Carrier':
			Airline = [0,0,0,0,0,1,0,0,0,0,0]
		if airline == 'Multi Carrier Eco':
			Airline = [0,0,0,0,0,0,1,0,0,0,0]
		if airline == 'Spice Jet':
			Airline = [0,0,0,0,0,0,0,1,0,0,0]
		if airline == 'True Jet':
			Airline = [0,0,0,0,0,0,0,0,1,0,0]
		if airline == 'Vistara':
			Airline = [0,0,0,0,0,0,0,0,0,1,0]
		if airline == 'Vistara Prem Eco':
			Airline = [0,0,0,0,0,0,0,0,0,0,1]

		if source != destination:
			#making final list
			input_list = [lst1 + FromCity + ToCity + Airline]
			#making prediction with trained model
			pred = model.predict(input_list)
			output = int(round(pred[0]))
			result = "The predicted Price is INR Rs.{}/-".format(output)
				
		else:
			result = "No such Route is Available!.."
	

		return render_template("result.html",prediction=result)
	return render_template("home.html")

	

if __name__=='__main__':
	app.run(host="0.0.0.0",port="5000")
