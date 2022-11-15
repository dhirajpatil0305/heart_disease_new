from project_app.utils import HeartDisease
from flask import Flask,render_template,request,jsonify
app=Flask(__name__)

@app.route("/") # HOME API
def hello_flask():
    print("hello python")
    return render_template("home.html")
@app.route("/predict_disease",methods=["POST"]) # TEST API
def predict_disease():
    data=request.form
    age=data["age"]
    sex=data["sex"]
    cp=data["cp"]
    trestbps=data["trestbps"]
    chol=data["chol"]
    fbs=data["fbs"]
    restecg=data["restecg"]
    thalach=data["thalach"]
    exang=data["exang"]
    oldpeak=data["oldpeak"]
    slope=data["slope"]
    ca=data["ca"]
    thal=data["thal"]
    disease=HeartDisease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    heart_disease=disease.get_predicted_disease()
    return jsonify({"THE PERSON HAVING HEART DISEASE OR NOT":int(heart_disease)})
if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=False)
