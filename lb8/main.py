import xml.etree.ElementTree as ET
import random
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

def generate_sales_data(sofas_data, base_sales=50, variance=10):
    for sofa in sofas_data:
        sales = [base_sales + random.randint(-variance, variance) for _ in range(12)]
        sofa["sales"] = sales
    return sofas_data

def select_random_sofas(sofas_data, num_sofas=3):
    return random.sample(sofas_data, num_sofas)

def select_test_sofa(sofas_data, training_sofas):
    remaining_sofas = [sofa for sofa in sofas_data if sofa not in training_sofas]
    return random.choice(remaining_sofas)

def predict_sales_sgd(training_data, test_data):
    X_train = []
    y_train = []

    for data in training_data:
        sales = data['sales']
        threshold = np.mean(sales)
        y = [1 if sale > threshold else 0 for sale in sales]
        X = np.array(range(1, 13)).reshape(-1, 1)
        X_train.extend(X)
        y_train.extend(y)

    model = SGDClassifier(alpha=0.001, random_state=42)
    model.fit(X_train, y_train)

    test_sales = test_data['sales']
    threshold = np.mean(test_sales)
    y_test_true = [1 if sale > threshold else 0 for sale in test_sales]

    X_test = np.array(range(1, 13)).reshape(-1, 1)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test_true, y_pred)
    conf_matrix = confusion_matrix(y_test_true, y_pred)

    return y_pred, y_test_true, accuracy, conf_matrix

def predict_sales_lr(training_data, test_data):
    X_train = []
    y_train = []

    for data in training_data:
        sales = data['sales']
        threshold = np.mean(sales)
        y = [1 if sale > threshold else 0 for sale in sales]
        X = np.array(range(1, 13)).reshape(-1, 1)
        X_train.extend(X)
        y_train.extend(y)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    test_sales = test_data['sales']
    threshold = np.mean(test_sales)
    y_test_true = [1 if sale > threshold else 0 for sale in test_sales]

    X_test = np.array(range(1, 13)).reshape(-1, 1)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test_true, y_pred)
    conf_matrix = confusion_matrix(y_test_true, y_pred)

    return y_pred, y_test_true, accuracy, conf_matrix

def main():
    xml_file = 'sofas.xml'

    sofas_data = read_xml(xml_file)

    sales_data = generate_sales_data(sofas_data, base_sales=50, variance=10)

    training_sofas = select_random_sofas(sales_data, num_sofas=3)
    print("Диваны:")
    for sofa in training_sofas:
        print(f"{sofa['model']} ({sofa['brand']})")

    test_sofa = select_test_sofa(sales_data, training_sofas)
    print("\nДиван для тестирования:")
    print(f"{test_sofa['model']} ({test_sofa['brand']})")

    # СГДшка
    sgd_predictions, y_test_true, sgd_accuracy, sgd_conf_matrix = predict_sales_sgd(training_sofas, test_sofa)
    print("\nSGDClassifier:")
    print(f"  Прогнозы: {sgd_predictions}")
    print(f"  Фактические данные: {y_test_true}")
    print(f"  Accuracy: {sgd_accuracy:.2f}")
    print("  Матрица ошибок:")
    print(sgd_conf_matrix)

    # Логик
    lr_predictions, y_test_true, lr_accuracy, lr_conf_matrix = predict_sales_lr(training_sofas, test_sofa)
    print("\nLogisticRegression:")
    print(f"  Прогнозы: {lr_predictions}")
    print(f"  Фактические данные: {y_test_true}")
    print(f"  Accuracy: {lr_accuracy:.2f}")
    print("  Матрица ошибок:")
    print(lr_conf_matrix)

if __name__ == "__main__":
    main()