import pandas as pd
import matplotlib.pyplot as plt
import os

# 0. 基础设置
plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
plt.rcParams['axes.unicode_minus'] = False

# 路径兜底（脚本在 notebooks/，CSV 在 data/）
BASE = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE, "..", "data", "global_superstore.csv")
output_dir = os.path.join(BASE, "..", "output")
os.makedirs(output_dir, exist_ok=True)  # 自动创建 output 文件夹

# 读取数据
df = pd.read_csv(csv_path, encoding="utf-8-sig")
# 基础清洗（报告对应）
print(f"缺失值统计：\n{df.isnull().sum()}")
df = df.drop_duplicates()  # 去重
df['Order Date'] = pd.to_datetime(df['Order Date'])  # 日期标准化
# 衍生指标（前序已用，此处统一）
df['Profit_Margin'] = df.apply(lambda x: x['Profit']/x['Sales'] if x['Sales']!=0 else 0, axis=1)


# 1. 数据概览
print(f"数据形状：{df.shape}")
print(f"列名：{df.columns.tolist()}")

# 2. 核心指标
print(f"\n总销售额：{df['Sales'].sum():,.2f}")
print(f"总利润：{df['Profit'].sum():,.2f}")

# 3. 地区利润
region_profit = df.groupby('Region')['Profit'].sum().sort_values()
print("\n各地区利润：")
print(region_profit)
plt.figure(figsize=(10, 6))
region_profit.plot(kind='barh', title='各地区利润对比')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "region_profit.png"))
plt.show()

# 4. 品类利润
category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
print("\n各品类利润：")
print(category_profit)
plt.figure(figsize=(8, 8))
category_profit.plot(kind='pie', autopct='%1.1f%%', title='各品类利润占比')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "category_profit.png"))
plt.show()

# 5. 亏损子品类 Top5
sub_cat_loss = df.groupby('Sub-Category')['Profit'].sum().sort_values().head(5)
print("\n亏损最严重子品类 Top5：")
print(sub_cat_loss)

# 6. 【新增】地区 × 品类 交叉分析（找“哪个地区卖家具最亏”）
print("\n【交叉分析】各地区各品类利润：")
cross_profit = df.pivot_table(index='Region', columns='Category', values='Profit', aggfunc='sum')
print(cross_profit)
plt.figure(figsize=(12, 7))
cross_profit.plot(kind='barh', title='各地区各品类利润对比')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "region_category_profit.png"))
plt.show()

# 7. 【新增】折扣率 vs 利润率 散点图（揭示 Tables 等亏损原因）
# 计算利润率，避免除零
df['Profit_Margin'] = df.apply(lambda x: x['Profit'] / x['Sales'] if x['Sales'] != 0 else 0, axis=1)
plt.figure(figsize=(10, 6))
plt.scatter(df['Discount'], df['Profit_Margin'], alpha=0.5)
plt.xlabel('折扣率 (Discount)')
plt.ylabel('利润率 (Profit/Sales)')
plt.title('折扣率与利润率关系（重点观察高折扣低利润区）')
plt.axhline(0, color='red', linestyle='--')  # 盈亏平衡线
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "discount_margin_scatter.png"))
plt.show()

# 8. 单独揪出 Tables 的折扣表现（结合你之前的亏损Top1）
tables_df = df[df['Sub-Category'] == 'Tables']
print(f"\n【Tables 洞察】平均折扣：{tables_df['Discount'].mean():.2f}，平均利润率：{tables_df['Profit_Margin'].mean():.2f}")

print("\n分析完成！所有图表已保存至 output 文件夹，可直接用于报告。")
