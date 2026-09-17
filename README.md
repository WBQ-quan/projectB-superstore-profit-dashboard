# Project B: Superstore Profit Dashboard

## 项目简介
基于 Superstore 销售数据的端到端利润分析，通过数据清洗、SQL 建模与可视化，定位利润流失核心原因。

## 技术栈
- **数据处理**：Python (Pandas), SQLite
- **数据库/查询**：SQLite (`superstore.db`), DBeaver (SQL)
- **可视化**：Power BI, Matplotlib
- **工程规范**：Git, `.gitignore` (排除大文件)

## 目录结构
projectB-superstore-profit-dashboard/
├── data/           # 原始数据 (xls/csv) & 数据库
├── sql/            # SQL 分析脚本
├── notebooks/      # Python 分析脚本
├── output/         # 图表输出 (png)
├── reports/        # 业务洞察 (md) & Power BI 源文件
└── README.md

## 核心结论（摘要）
- 利润低主要集中在某些子类别（如桌子）与特定区域。
- 高折扣并未带来足够销量增长，反而拉低整体利润率。
（详细见 `reports/superstore_insights.md`）

## 运行说明
1. 数据已落库至 `data/superstore.db`（本地不提交，见 `.gitignore`）。
2. SQL 脚本位于 `sql/`，可通过 DBeaver 执行。
3. Power BI 看板源文件位于 `reports/`（本地不提交）。
