import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def calculate_total_sales(data):
    total_sales = sum(float(row['jumlah']) for row in data)
    return total_sales

def find_highest_sales_transaction(data):
    highest_sales = max(data, key=lambda row: float(row['jumlah']))
    return highest_sales

def count_transactions(data):
    total_transactions = len(data)
    return total_transactions

def find_sold_products(data):
    sold_products = set(row['produk'] for row in data if float(row['jumlah']) > 0)
    return sold_products


# Contoh penggunaan skrip
file_path = 'transaksi.csv'
data = read_csv_file(file_path)

total_sales = calculate_total_sales(data)
highest_sales_transaction = find_highest_sales_transaction(data)
total_transactions = count_transactions(data)
sold_products = find_sold_products(data)

print("Total Penjualan: ", total_sales)
print("Transaksi dengan Penjualan Tertinggi: ", highest_sales_transaction)
print("Jumlah Transaksi: ", total_transactions)
print("Daftar Produk yang Terjual: ", sold_products)
