from flask import Flask, render_template , request
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])

def index():
    if request.method=='POST':
        height=float(request.form['height'])
        weight=float(request.form['weight'])
        bmi=round(weight/((height/100)**2),3)
        return render_template('home.html',bmi=bmi)
    return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)

    


