import pandas as pd

# 读取（严格匹配大小写和空格，用绝对路径最稳）
file_path = r"D:\GlobalSuperstore\data_analysis_projects\superstore-analysisi\data\global superstore.xls"
df = pd.read_excel(file_path, sheet_name="Orders", engine="xlrd")

# 转存 CSV 到 data 文件夹（同目录）
df.to_csv(r"D:\GlobalSuperstore\data_analysis_projects\superstore-analysisi\data\global_superstore.csv", index=False, encoding="utf-8-sig")

print(f"转换成功！共读取 {df.shape[0]} 行，{df.shape[1]} 列。")
