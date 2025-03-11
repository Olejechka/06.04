import xml.etree.ElementTree as ET
import random
import pandas as pd
import matplotlib.pyplot as plt


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

def generate_sales_data(sofas_data):
    for sofa in sofas_data:
        sales = [random.randint(10, 100) for _ in range(12)]
        sofa["sales"] = sales
    return sofas_data

def predict_sales_13th_month(sales_data):
    predictions = []
    for sofa in sales_data:
        last_three_months = sofa["sales"][-3:]
        predicted_sales = round(sum(last_three_months) / len(last_three_months))
        predictions.append({
            "model": sofa["model"],
            "brand": sofa["brand"],
            "price": sofa["price"],
            "predicted_sales": predicted_sales
        })
    return predictions

def analyze_trend(sales_data):
    trends = []
    for sofa in sales_data:
        sales = sofa["sales"]
        avg_sales = sum(sales) / len(sales)
        last_month_sales = sales[-1]

        if last_month_sales > avg_sales:
            trend = "Рост"
        elif last_month_sales < avg_sales:
            trend = "Снижение"
        else:
            trend = "Стабильность"
        trends.append({
            "model": sofa["model"],
            "brand": sofa["brand"],
            "trend": trend
        })
    return trends


def visualize_data_with_prediction(sales_data, predictions):
    for data in sales_data:
        plt.plot(range(1, 13), data['sales'], label=f"{data['model']} (история)")
    for pred in predictions:
        plt.scatter(13, pred["predicted_sales"], color='red', label=f"{pred['model']} (прогноз)")

    plt.xlabel('Месяцы')
    plt.ylabel('Продажи')
    plt.title('Динамика продаж моделей диванов')
    plt.legend()
    plt.show()

def display_table_with_predictions(data, predictions):
    rows = []
    for sofa, pred in zip(data, predictions):
        row = {
            "Модель": sofa["model"],
            "Бренд": sofa["brand"],
            "Цена": sofa["price"],
            **{f"Месяц {i + 1}": sale for i, sale in enumerate(sofa["sales"])},
            "Прогноз": pred["predicted_sales"]
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    display(df)
def main():
    xml_file = 'sofas.xml'
    sofas_data = read_xml(xml_file)
    sales_data = generate_sales_data(sofas_data)
    predictions = predict_sales_13th_month(sales_data)
    trends = analyze_trend(sales_data)
    for trend in trends:
        print(f"Модель: {trend['model']}, Тренд: {trend['trend']}")
    visualize_data_with_prediction(sales_data, predictions)
    display_table_with_predictions(sales_data, predictions)
if __name__ == "__main__":
    main()