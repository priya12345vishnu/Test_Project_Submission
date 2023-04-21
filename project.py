from flask import flask, render_template, request
import numpy as np
import pickle
app=flask(_name_)
model=pickle.load(open(r’rdf.pkl’,’rb’))
scale=pickle.load(open(r’scale1.pkl’,’rb’))
@app.route(‘/’)
Def home:
     Return render_template(‘home.html’)

@app.route('/') # rendering the html template
def home():
   return render_template('home.html')

@app.route('/submit',methods=["POST","GET"])# route to show the prediction in a web UI
def submit():
   # reading the inputs givenby the user
   input_feature=[int(x) for x in request.form.values()]
   #input feature=np.transpose(input_feature)
   input feature=[np.array(input_feature)]
   print(input_feature)
   names=['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_amount_Term','Credit_history','Property_Area']
   data=pandas.DataFrame(input_feature,columns=names)
   print(data)


   #data_scaled=scale.fit_transform(data)
   #data=pandas.DataFrame(,columns=names)

   #predictions using the loaded modelfile
   prediction=model.predict(data)
   print(prediction=int(prediction)
   print(type(prediction))

   if(prediction==0):
       return render_template("output.html",result="Loan will not be Approved")
   else:
      return render_template("output.html",result="Loan will be Approved")
   #showing the prediction results in a UI
if_name_=="_main_":
   # app.run(host='0.0.0.0',port=8000,debug=True)        #running the app
port=int(os.environ.get('PORT',5000))
app.run(debug=False)












