# Project B: Superstore Profit Dashboard

## 项目简介
基于全球超市（Superstore）业务数据的利润分析与可视化仪表盘。通过 Python 进行数据清洗与转换，结合 SQL 分析，最终使用 Power BI 呈现多维度利润洞察。

## 目录结构
- `data/`: 原始数据与转换后的 CSV
- `notebooks/`: Python 数据分析与处理脚本（如 `convert_to_csv.py`）
- `sql/`: SQL 分析查询语句
- `output/`: 图表与可视化输出（如利润散点图、区域利润图）
- `reports/`: 分析报告（Markdown/文档）
- `*.pbix`: Power BI 仪表盘源文件（已被 .gitignore 过滤，可选保留）

## 核心功能
- 数据清洗：Excel 转 CSV，统一编码与格式
- 利润分析：折扣与利润关系、各区域/类别利润表现
- 可视化：Python 生成静态图表 + Power BI 交互式仪表盘

## 使用说明
1. 克隆仓库：`git clone https://github.com/WBQ-quan/projectB-superstore-profit-dashboard.git`
2. 运行 `notebooks/convert_to_csv.py` 生成标准 CSV
3. 查看 `reports/superstore_insights.md` 获取分析结论
4. 打开 Power BI 文件（若保留）浏览仪表盘

## 技术栈
Python (Pandas) · SQL · Power BI · Git
