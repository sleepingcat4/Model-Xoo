# Import necessary modules
from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/datasets')
def datasets():
    # Define your dataset links here
    dataset_links = [
        {'name': 'Dataset 1', 'link': 'http://example.com/dataset1'},
        {'name': 'Dataset 2', 'link': 'http://example.com/dataset2'}
    ]
    return render_template('datasets.html', dataset_links=dataset_links)

@app.route('/models')
def models():
    # Define your model links here
    model_links = [
        {'name': 'Model 1', 'link': 'http://example.com/model1'},
        {'name': 'Model 2', 'link': 'http://example.com/model2'}
    ]
    return render_template('models.html', model_links=model_links)

# Run the app
if __name__ == '__main__':
    app.run(debug=False)
