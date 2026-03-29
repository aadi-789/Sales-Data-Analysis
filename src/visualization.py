import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Style
sns.set(style="whitegrid")


# -------------------------------
# 1. CUSTOMER ANALYSIS
# -------------------------------
def plot_top_customers(df, path):
    df_top = df.sort_values(by="total_sales", ascending=False).head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x='total_sales', y='customer_name', data=df_top)
    plt.title("Top Customers by Sales")
    plt.tight_layout()
    plt.savefig(path + "top_customers.png")
    plt.close()


# -------------------------------
# 2. DELIVERY ANALYSIS
# -------------------------------
def plot_delivery(df, path):
    plt.figure(figsize=(10,6))
    sns.barplot(x='segment_label', y='avg_delivery_days', data=df)
    plt.title("Delivery Time by Customer Segment")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(path + "delivery_analysis.png")
    plt.close()


# -------------------------------
# 3. DISCOUNT VS PROFIT
# -------------------------------
def plot_discount(df, path):
    plt.figure(figsize=(10,6))
    sns.lineplot(x='discount', y='avg_profit', data=df, marker='o')
    plt.title("Discount vs Profit")
    plt.tight_layout()
    plt.savefig(path + "discount_vs_profit.png")
    plt.close()


# -------------------------------
# 4. HIGH DISCOUNT LOSS
# -------------------------------
def plot_high_discount_loss(df, path):
    plt.figure(figsize=(10,6))
    sns.histplot(df['discount'], bins=20, kde=True)
    plt.title("High Discount Loss Distribution")
    plt.xlabel("Discount")
    plt.tight_layout()
    plt.savefig(path + "high_discount_loss.png")
    plt.close()


# -------------------------------
# 5. LOSS MAKING PRODUCTS
# -------------------------------
def plot_loss_making_products(df, path):
    top_loss = df.nsmallest(10, 'profit_margin')

    plt.figure(figsize=(10,6))
    sns.barplot(x='profit_margin', y='category', data=top_loss)
    plt.title("Top Loss-Making Products")
    plt.tight_layout()
    plt.savefig(path + "loss_products.png")
    plt.close()


# -------------------------------
# 6. MOM GROWTH (Month over Month)
# -------------------------------
def plot_mom_growth(df, path):
    df['month'] = pd.to_datetime(df['month'])

    plt.figure(figsize=(12,6))
    sns.lineplot(x='month', y='growth_percentage', data=df, marker='o')
    plt.title("Month-over-Month Growth (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(path + "mom_growth.png")
    plt.close()


# -------------------------------
# 7. MONTHLY SALES TREND
# -------------------------------
def plot_sales_trend(df, path):
    df['month'] = pd.to_datetime(df['month'])

    plt.figure(figsize=(12,6))
    plt.plot(df['month'], df['sales'])
    plt.title("Monthly Sales Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(path + "monthly_sales.png")
    plt.close()


# -------------------------------
# 8. CATEGORY PROFIT
# -------------------------------
def plot_category_profit(df, path):
    plt.figure(figsize=(8,5))
    sns.barplot(x='category', y='profit_margin', data=df)
    plt.title("Profit margin by Category (%)")
    plt.tight_layout()
    plt.savefig(path + "category_profit.png")
    plt.close()




# -------------------------------
# 9. REGION ANALYSIS
# -------------------------------
def plot_region(df, path):
    plt.figure(figsize=(8,5))
    sns.barplot(x='region', y='total_sales', data=df)
    plt.title("Sales by Region")
    plt.tight_layout()
    plt.savefig(path + "region_sales.png")
    plt.close()


# -------------------------------
# 10. RFM SEGMENTATION
# -------------------------------
def plot_rfm(df, path):
    plt.figure(figsize=(10,6))
    sns.countplot(x='customer_segment', data=df)
    plt.title("Customer Segments (RFM)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(path + "rfm_segments.png")
    plt.close()


# -------------------------------
# 11. STATE ANALYSIS
# -------------------------------
def plot_state_analysis(df, path):
    top_states = df.nlargest(10, 'sum')

    plt.figure(figsize=(10,6))
    sns.barplot(x='sum', y='state', data=top_states)
    plt.title("Top 10 States by Sales")
    plt.tight_layout()
    plt.savefig(path + "state_sales.png")
    plt.close()


# -------------------------------
# 12. YEARLY TREND
# -------------------------------
def plot_yearly_trend(df, path):
    plt.figure(figsize=(8,5))
    sns.lineplot(x='year', y='total_sales', data=df, marker='o')
    plt.title("Yearly Sales Trend")
    plt.tight_layout()
    plt.savefig(path + "yearly_sales.png")
    plt.close()


# -------------------------------
# 13. CORRELATION MATRIX
# -------------------------------
def plot_correlation(df, path):
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True)
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.savefig(path + "correlation.png")
    plt.close()