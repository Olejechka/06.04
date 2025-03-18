import xml.etree.ElementTree as ET
import random
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    sofas_data = []
    for sofa in root.findall('sofa'):
        model = sofa.find('model').text
        brand = sofa.find('brand').text
        price = int(sofa.find('price').text)
        sofas_data.append({"model": model, "brand": brand, "price": price})
    return sofas_data

def select_random_sofas(sofas_data, num_sofas=2):
    return random.sample(sofas_data, num_sofas)

def generate_sales_data(sofas_data):
    for sofa in sofas_data:
        sales = [random.randint(10, 100) for _ in range(12)]
        sofa["sales"] = sales
    return sofas_data

def write_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def predict_future_sales_sgd(sales_data):
    predictions = []

    for data in sales_data:
        sales = data['sales']

        threshold = np.mean(sales)
        y = [1 if sale > threshold else 0 for sale in sales]

        X = np.array(range(1, 13)).reshape(-1, 1)

        model = SGDClassifier(alpha=0.001, random_state=42)
        model.fit(X, y)
        future_X = np.array([[13]])
        future_prediction = model.predict(future_X)[0]
        data['predicted_sales_sgd'] = future_prediction
        predictions.append(data)

    return predictions

def predict_future_sales_lr(sales_data):
    predictions = []

    for data in sales_data:
        sales = data['sales']
        threshold = np.mean(sales)
        y = [1 if sale > threshold else 0 for sale in sales]
        X = np.array(range(1, 13)).reshape(-1, 1)

        model = LogisticRegression()
        model.fit(X, y)

        future_X = np.array([[13]])
        future_prediction = model.predict_proba(future_X)[0][1]

        data['predicted_sales_lr'] = future_prediction
        predictions.append(data)

    return predictions

def visualize_data(sales_data):
    for data in sales_data:
        plt.plot(range(1, 13), data['sales'], label=f"{data['model']} (фактические)")
        plt.scatter([13], [data['predicted_sales_sgd']], label=f"{data['model']} (SGD)", color='red')
        plt.scatter([13], [data['predicted_sales_lr']], label=f"{data['model']} (Логический)", color='green')

    plt.xlabel('Месяцы')
    plt.ylabel('Продажи / Вероятность')
    plt.title('Динамика продаж моделей диванов и прогноз')
    plt.legend()
    plt.show()

def compare_models(sales_data):
    print("Сравнение метрик качества:")
    for data in sales_data:
        sales = data['sales']
        threshold = np.mean(sales)
        y_true = [1 if sale > threshold else 0 for sale in sales]

        y_pred_sgd = [data['predicted_sales_sgd']] * len(y_true)
        accuracy_sgd = accuracy_score(y_true, y_pred_sgd)
        conf_matrix_sgd = confusion_matrix(y_true, y_pred_sgd)

        print(f"Модель {data['model']} (SGD):")
        print(f"  Accuracy: {accuracy_sgd:.2f}")
        print("  Матрица ошибок:")
        print(conf_matrix_sgd)

        y_pred_lr = [1 if data['predicted_sales_lr'] > 0.5 else 0] * len(y_true)
        accuracy_lr = accuracy_score(y_true, y_pred_lr)
        conf_matrix_lr = confusion_matrix(y_true, y_pred_lr)

        print(f"Модель {data['model']} (Логический):")
        print(f"  Accuracy: {accuracy_lr:.2f}")
        print("  Матрица ошибок:")
        print(conf_matrix_lr)
def main():
    xml_file = 'sofas.xml'
    json_file = 'sofas_sales.json'

    sofas_data = read_xml(xml_file)
    selected_sofas = select_random_sofas(sofas_data, num_sofas=2)
    print("Выбранные диваны:")
    for sofa in selected_sofas:
        print(f"{sofa['model']} ({sofa['brand']})")
    sales_data = generate_sales_data(selected_sofas)
    write_json(json_file, sales_data)

    predicted_data_sgd = predict_future_sales_sgd(sales_data.copy())
    predicted_data_lr = predict_future_sales_lr(sales_data.copy())

    for sgd_data, lr_data in zip(predicted_data_sgd, predicted_data_lr):
        sgd_data['predicted_sales_lr'] = lr_data['predicted_sales_lr']
    visualize_data(predicted_data_sgd)
    compare_models(predicted_data_sgd)

if __name__ == "__main__":
    main()