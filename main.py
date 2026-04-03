import os
print("Available files" , os.listdir("outputs/processed/"))

from src.data_loader import load_data
from src.visualization import *

DATA_PATH = "outputs/processed/"
OUTPUT_PATH = "outputs/charts/"

customers = load_data(DATA_PATH + "combined_customer_ranking.csv")
delivery = load_data(DATA_PATH + "delivery_analysis.csv")
discount = load_data(DATA_PATH + "discount_vs_profit_analysis.csv")
high_discount = load_data(DATA_PATH + "high_discount_loss_analysis.csv")
loss_products = load_data(DATA_PATH + "loss_making_products.csv")
mom_growth = load_data(DATA_PATH + "mom_growth.csv")
sales = load_data(DATA_PATH + "monthly_sales.csv")
category = load_data(DATA_PATH + "profit_category.csv")

region = load_data(DATA_PATH + "region_wise_analysis.csv")
rfm = load_data(DATA_PATH + "rfm_analysis.csv")
state = load_data(DATA_PATH + "state_wise_analysis.csv")
yearly_trend = load_data(DATA_PATH + "yearly_sales_trend.csv")

plot_top_customers(customers, OUTPUT_PATH)
plot_delivery(delivery, OUTPUT_PATH)
plot_discount(discount, OUTPUT_PATH)
plot_high_discount_loss(high_discount, OUTPUT_PATH)
plot_loss_making_products(loss_products, OUTPUT_PATH)
plot_mom_growth(mom_growth, OUTPUT_PATH)
plot_sales_trend(sales, OUTPUT_PATH)
plot_category_profit(category, OUTPUT_PATH)

plot_region(region, OUTPUT_PATH)
plot_rfm(rfm, OUTPUT_PATH)
plot_state_analysis(state, OUTPUT_PATH)
plot_yearly_trend(yearly_trend, OUTPUT_PATH)

plot_correlation(sales, OUTPUT_PATH)

print("✅ All 13 visuals generated successfully!")