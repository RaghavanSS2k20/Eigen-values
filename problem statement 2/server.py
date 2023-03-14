from flask import *
from getip import get_ip
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
response = dict()
app = Flask(__name__)
allowed_flag = False
@app.route('/')
def index():
    


    return {'message':'app has been setup'}
@app.route('/getip')
def getip():
    ip = get_ip()
    return ip

@app.route('/classifier/metrics', methods=['GET'])
def get_metrics():
    from ml import metrics
    response={
        'model':'Decision tree',
        'metrics':metrics
    }
    return jsonify(response)
@app.route('/cnn/metrics')
def get_cnn_metrics():
    from cnn import performance_measures
    metrics = performance_measures
    response={
        'model':'CNN',
        'metrics': metrics
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
    
