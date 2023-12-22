from flask import Flask, render_template, request
from joblib import load
import numpy as np

app = Flask(__name__)

# Load your trained model or any other necessary components
loaded_pipeline = load('full_pipeline.joblib')
loaded_model = load('knn_model.joblib')
loaded_model1 = load('dt_model.joblib')
loaded_modelsvm = load('svm_model-2.joblib')
loaded_modelbs = load('nb_model.joblib')
loaded_modellr = load('lr_model2.joblib')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dt')
def render_dt():
    return render_template('dt.html')

@app.route('/svm')
def render_svm():
    return render_template('svm.html')

@app.route('/bs')
def render_bs():
    return render_template('bs.html')

@app.route('/lr')
def render_lr():
    return render_template('lr.html')



@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        feature_names = [
            'duration', 'src_bytes', 'dst_bytes', 'wrong_fragment', 'logged_in',
            'num_file_creations', 'count', 'srv_count', 'diff_srv_rate',
            'srv_diff_host_rate', 'dst_host_count', 'dst_host_diff_srv_rate',
            'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
            'service_ecr_i', 'service_finger', 'service_ftp_data', 'service_other',
            'service_private', 'service_smtp', 'service_telnet', 'flag_RSTO', 'flag_RSTR'
        ]
        # Extract features from the form data
        features = [float(request.form.get(f)) for f in feature_names]

        # Transform the input features using the loaded pipeline
        transformed_features = loaded_pipeline.transform([features])

        predicted_label = predict_class(transformed_features)

        # Map predicted labels to categories
        translated_label = map_label(predicted_label)

        return render_template('result.html', prediction=translated_label)
def map_label(label):
    label_map = {
        0: 'Normal',
        1: 'DoS',
        2: 'Probe',
        3: 'R2L',
        4: 'U2L'
        # Add more mappings if needed
    }
    return label_map.get(label)

def predict_class(new_data):
    # Assuming 'new_data' is a list of features for prediction
    predicted_class = loaded_model.predict(new_data)[0]
    return predicted_class


@app.route('/predict_dt', methods=['POST'])
def predict_dt():
    if request.method == 'POST':
        feature_names = [
            'duration', 'src_bytes', 'dst_bytes', 'wrong_fragment', 'logged_in',
            'num_file_creations', 'count', 'srv_count', 'diff_srv_rate',
            'srv_diff_host_rate', 'dst_host_count', 'dst_host_diff_srv_rate',
            'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
            'service_ecr_i', 'service_finger', 'service_ftp_data', 'service_other',
            'service_private', 'service_smtp', 'service_telnet', 'flag_RSTO', 'flag_RSTR'
        ]
        # Extract features from the form data
        features = [float(request.form.get(f)) for f in feature_names]

        # Transform the input features using the loaded pipeline
        transformed_features = loaded_pipeline.transform([features])

        predicted_label = predict_class_dt(transformed_features)

        # Map predicted labels to categories
        translated_label = map_label(predicted_label)

        return render_template('result_dt.html', prediction=translated_label)
def predict_class_dt(new_data):
    # Assuming 'new_data' is a list of features for prediction
    predicted_class = loaded_model1.predict(new_data)[0]
    return predicted_class




@app.route('/predict_svm', methods=['POST'])
def predict_svm():
    if request.method == 'POST':
        feature_names = [
            'duration', 'src_bytes', 'dst_bytes', 'wrong_fragment', 'logged_in',
            'num_file_creations', 'count', 'srv_count', 'diff_srv_rate',
            'srv_diff_host_rate', 'dst_host_count', 'dst_host_diff_srv_rate',
            'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
            'service_ecr_i', 'service_finger', 'service_ftp_data', 'service_other',
            'service_private', 'service_smtp', 'service_telnet', 'flag_RSTO', 'flag_RSTR'
        ]
        # Extract features from the form data
        features = [float(request.form.get(f)) for f in feature_names]

        # Transform the input features using the loaded pipeline
        transformed_features = loaded_pipeline.transform([features])

        predicted_label = predict_class_svm(transformed_features)

        # Map predicted labels to categories
        translated_label = map_label(predicted_label)

        return render_template('result_svm.html', prediction=translated_label)
def predict_class_svm(new_data):
    # Assuming 'new_data' is a list of features for prediction
    predicted_class = loaded_modelsvm.predict(new_data)[0]
    return predicted_class







@app.route('/predict_bs', methods=['POST'])
def predict_bs():
    if request.method == 'POST':
        feature_names = [
            'duration', 'src_bytes', 'dst_bytes', 'wrong_fragment', 'logged_in',
            'num_file_creations', 'count', 'srv_count', 'diff_srv_rate',
            'srv_diff_host_rate', 'dst_host_count', 'dst_host_diff_srv_rate',
            'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
            'service_ecr_i', 'service_finger', 'service_ftp_data', 'service_other',
            'service_private', 'service_smtp', 'service_telnet', 'flag_RSTO', 'flag_RSTR'
        ]
        # Extract features from the form data
        features = [float(request.form.get(f)) for f in feature_names]

        # Transform the input features using the loaded pipeline
        transformed_features = loaded_pipeline.transform([features])

        predicted_label = predict_class_bs(transformed_features)

        # Map predicted labels to categories
        translated_label = map_label(predicted_label)

        return render_template('result_svm.html', prediction=translated_label)
def predict_class_bs(new_data):
    # Assuming 'new_data' is a list of features for prediction
    predicted_class = loaded_modelbs.predict(new_data)[0]
    return predicted_class















@app.route('/predict_lr', methods=['POST'])
def predict_lr():
    if request.method == 'POST':
        feature_names = [
            'duration', 'src_bytes', 'dst_bytes', 'wrong_fragment', 'logged_in',
            'num_file_creations', 'count', 'srv_count', 'diff_srv_rate',
            'srv_diff_host_rate', 'dst_host_count', 'dst_host_diff_srv_rate',
            'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
            'service_ecr_i', 'service_finger', 'service_ftp_data', 'service_other',
            'service_private', 'service_smtp', 'service_telnet', 'flag_RSTO', 'flag_RSTR'
        ]
        # Extract features from the form data
        features = [float(request.form.get(f)) for f in feature_names]

        # Transform the input features using the loaded pipeline
        transformed_features = loaded_pipeline.transform([features])

        predicted_label = predict_class_lr(transformed_features)

        # Map predicted labels to categories
        translated_label = map_label(predicted_label)

        return render_template('result_lr.html', prediction=translated_label)
def predict_class_lr(new_data):
    # Assuming 'new_data' is a list of features for prediction
    predicted_class = loaded_modellr.predict(new_data)[0]
    return predicted_class



if __name__ == '__main__':
    app.run(debug=True)



