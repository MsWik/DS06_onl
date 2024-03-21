from flask import Flask, request, jsonify

app = Flask(__name__)
import pickle

# Загрузка модели из файла
with open('cat_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


@app.route('/predict', methods=['POST'])   #:/predict
def predict():
    # Получаем данные для предсказания из POST запроса
    data = request.get_json(force=True)
    predict_request = [data[key] for key in ['Store', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI',\
       'Unemployment', 'day_of_week', 'month']]
    
    # Делаем предсказание с помощью модели
    prediction = model.predict([predict_request])[0]

    # Возвращаем результат
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
