import pandas as pd

invoices = pd.read_csv("data/raw/invoices.csv", skiprows=3)
# print(invoices.shape)
# print(invoices.head())

invoices = invoices[invoices["date"] != "TOTAL"]
invoices["voucherNumber"] = invoices["voucherNumber"].astype(int)
print(invoices.shape)
print(invoices.head())


items = pd.read_csv("data/raw/invoice_items.csv", skiprows=3)
items = items[items["date"] != "TOTAL"]
items["voucherNumber"] = items["voucherNumber"].astype(int)
print(items.shape)
print(items.head())