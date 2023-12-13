from flask import Flask,jsonify,request, render_template
from Static import utils
import repository
app = Flask(__name__,template_folder='Templates',static_folder='Static')


@app.route('/chart1')
def Chart1():
   
    return render_template('chart1.html')

@app.route('/chart2')
def Chart2():
    db = repository.MongDB_API()
    data =  db.chart1()
    print(jsonify(data))
    return render_template('chart2.html')

@app.route('/chart3')
def Chart3():
    return render_template('chart3.html')

@app.route('/chart4')
def Chart4():
    return render_template('chart4.html')
@app.route('/chart5')
def Chart5():
    return render_template('chart5.html')

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/getchartdata/<int:chartnum>')
def get_chart_data(chartnum):
    db = repository.MongDB_API()
    
    if chartnum ==1:
        data = db.chart1()
    
    elif chartnum ==2 :
        data = db.chart2()
    
    elif chartnum == 3 :
        data = db.chart3()
    
    elif chartnum ==4:
        data = db.chart4()
    
    elif chartnum ==5:
        data = db.chart5()

    else:
        data = {}

    return jsonify(data)


if __name__ =="__main__":
    app.run(host="0.0.0.0",port=3000)